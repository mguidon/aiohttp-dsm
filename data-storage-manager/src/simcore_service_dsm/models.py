import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


metadata = sa.MetaData()

# File meta data
file_meta_data = sa.Table(
    "file_meta_data", metadata,
    sa.Column("object_name", sa.String, primary_key=True),
    sa.Column("bucket_name", sa.String),
    sa.Column("file_id", sa.String), #uuid
    sa.Column("file_name", sa.String),
    sa.Column("user_id", sa.Integer),
    sa.Column("user_name", sa.String),
    sa.Column("location", sa.String),
    sa.Column("project_id", sa.Integer),
    sa.Column("project_name", sa.String),
    sa.Column("node_id", sa.Integer),
    sa.Column("node_name", sa.String),
)

class FileMetaData:
    def __init__(self, object_name: str, bucket_name ="", file_id: str="", file_name: str="", user_id: int=-1, user_name: str="", location: str="", project_id: int=-1,
            project_name: str="", node_id: int=-1, node_name: str="", **kargs):
        
        self.object_name = object_name
        self.bucket_name = bucket_name
        self.file_id = file_id
        self.file_name = file_name
        self.user_id = user_id
        self.user_name =user_name
        self.location = location
        self.project_id = project_id
        self.project_name = project_name
        self.node_id = node_id
        self.node_name = node_name


