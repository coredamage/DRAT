#------------------------------------------------------------------------------
# DRAT Prototype Tool Source Code
# 
# Copyright 2019 Carnegie Mellon University. All Rights Reserved.
# 
# NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING 
# INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON
# UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS
# TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE
# OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE
# MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND
# WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
# 
# Released under a MIT (SEI)-style license, please see license.txt or contact
# permission@sei.cmu.edu for full terms.
# 
# [DISTRIBUTION STATEMENT A] This material has been approved for public
# release and unlimited distribution.  Please see Copyright notice for non-US
# Government use and distribution.
# 
# This Software includes and/or makes use of the following Third-Party
# Software subject to its own license:
# 
# 1. Python 3.7 (https://docs.python.org/3/license.html)
# Copyright 2001-2019 Python Software Foundation.
# 
# 2. SQL Alchemy (https://github.com/sqlalchemy/sqlalchemy/blob/master/LICENSE)
# Copyright 2005-2019 SQLAlchemy authors and contributor.
# 
# DM19-0055
#------------------------------------------------------------------------------

"""Added FileDetailStorage to database.

Revision ID: bbf892f6d96f
Revises: a3c47f0e9b96
Create Date: 2018-08-30 09:11:56.614443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbf892f6d96f'
down_revision = 'a3c47f0e9b96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file_detail_storage_link',
    sa.Column('id', sa.BigInteger(), nullable=False, comment="Primary key for FileDetailStorageLink"),
    sa.Column('file_storage_id', sa.Integer(), nullable=True, comment="Foreign key to file_storage.file_storage_id"),
    sa.Column('file_detail_id', sa.Integer(), nullable=True, comment="Foreign key to file_detail.file_detail_id"),
    sa.Column('file_type', sa.String(length=1), nullable=False, comment="Specifies file type; O=Original from rpm, C=Current from system."),
    sa.CheckConstraint("file_type in ('O', 'C')", name='file_detail_storage_link_c01'),
    sa.ForeignKeyConstraint(['file_detail_id'], ['file_detail.file_detail_id'], ),
    sa.ForeignKeyConstraint(['file_storage_id'], ['file_storage.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('file_detail_id', 'file_type', name='file_detail_storage_link_u02'),
    sa.UniqueConstraint('file_storage_id', 'file_detail_id', name='file_detail_storage_link_u01')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('file_detail_storage_link')
    # ### end Alembic commands ###
