from s3wrapper.s3_client import S3Client

import asyncio
from aiopg.sa import create_engine

from .models import FileMetaData, file_meta_data

import sqlalchemy as sa

import re
from operator import itemgetter

from typing import List, Tuple
FileMetaDataVec = List[FileMetaData]
Query = Tuple[str, str] # attibute name, regex

class Dsm:
    def __init__(self, db_endpoint: str, s3_client: S3Client):
        self.db_endpoint = db_endpoint
        self.s3_client = s3_client

    async def list_files(self, user_id: int, location: str, regex: str="", sortby: str="") -> FileMetaDataVec:
        data = []
        async with create_engine(self.db_endpoint) as engine:
            async with engine.acquire() as conn:
                query = sa.select([file_meta_data]).where(file_meta_data.c.user_id == user_id)
                async for row in conn.execute(query):
                    result_dict = dict(zip(row._result_proxy.keys, row._row))
                    d = FileMetaData(**result_dict)
                    data.append(d)

        if sortby:
            data = sorted(data, key=itemgetter(sortby)) 

        if regex:
            _query = re.compile(regex, re.IGNORECASE)
            filtered_data = []
            for d in data:
                _vars = vars(d)
                for v in _vars.keys():
                    if _query.search(v) or _query.search(str(_vars[v])):
                        filtered_data.append(d)
                        break
            return filtered_data
        
        return data


    async def delete_file(self, user_id: int, location: str, file_id: str):
        # get the file path
        async with create_engine(self.db_endpoint) as engine:
            async with engine.acquire() as conn:
                query = sa.select([file_meta_data]).where(file_meta_data.c.file_id == file_id)
                async for row in conn.execute(query):
                    result_dict = dict(zip(row._result_proxy.keys, row._row))
                    d = FileMetaData(**result_dict)
                    # make sure this is the current user
                    if d.user_id == user_id:
                        # threaded please
                        if self.s3_client.remove_objects(d.bucket_name, [d.object_name]):
                            stmt = file_meta_data.delete().where(file_meta_data.c.file_id == file_id)
                            await conn.execute(stmt) 


    def upload_file(self):
        pass

    def download_file(self):
        pass

    async def upload_link(self, fmd : FileMetaData):
         async with create_engine(self.db_endpoint) as engine:
            async with engine.acquire() as conn:
                ins = file_meta_data.insert().values(**vars(fmd))
                await conn.execute(ins)
                return self.s3_client.create_presigned_put_url(fmd.bucket_name, fmd.object_name)
        
    def download_link(self, fmd : FileMetaData):
        return self.s3_client.create_presigned_get_url(fmd.bucket_name, fmd.object_name)