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

"""Disabled nulls in link tables

Revision ID: f00ae5662f79
Revises: 0ed10325dade
Create Date: 2018-08-30 16:44:50.640940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f00ae5662f79'
down_revision = '0ed10325dade'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('file_detail_storage_link', 'file_detail_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('file_detail_storage_link', 'file_storage_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('rpm_file_detail_link', 'file_detail_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('rpm_file_detail_link', 'rpm_detail_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rpm_file_detail_link', 'rpm_detail_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.alter_column('rpm_file_detail_link', 'file_detail_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.alter_column('file_detail_storage_link', 'file_storage_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('file_detail_storage_link', 'file_detail_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
