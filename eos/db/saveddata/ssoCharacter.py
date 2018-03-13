# ===============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of eos.
#
# eos is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# eos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with eos.  If not, see <http://www.gnu.org/licenses/>.
# ===============================================================================

from sqlalchemy import Table, Column, Integer, String, DateTime, UniqueConstraint, ForeignKey
from sqlalchemy.orm import mapper
import datetime

from eos.db import saveddata_meta
from eos.saveddata.ssocharacter import SsoCharacter

sso_table = Table("ssoCharacter", saveddata_meta,
                    Column("ID", Integer, primary_key=True),
                    Column("client", String, nullable=False),
                    Column("characterID", Integer, nullable=False),
                    Column("characterName", String, nullable=False),
                    Column("refreshToken", String, nullable=False),
                    Column("accessToken", String, nullable=False),
                    Column("accessTokenExpires", DateTime, nullable=False),
                    Column("created", DateTime, nullable=True, default=datetime.datetime.now),
                    Column("modified", DateTime, nullable=True, onupdate=datetime.datetime.now),
                    UniqueConstraint('client', 'characterID', name='uix_client_characterID'),
                    UniqueConstraint('client', 'characterName', name='uix_client_characterName')
                  )

sso_character_map_table = Table("ssoCharacterMap", saveddata_meta,
                    Column("characterID", ForeignKey("characters.ID"), primary_key=True),
                    Column("ssoCharacterID", ForeignKey("ssoCharacter.ID"), primary_key=True),
                  )

mapper(SsoCharacter, sso_table)