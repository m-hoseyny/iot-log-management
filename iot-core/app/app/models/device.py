from typing import TYPE_CHECKING
import uuid, datetime

from sqlalchemy import Column, String, JSON, UniqueConstraint, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class Device(Base):
    __tablename__ = 'devices'
    __table_args__ = (
        # this can be db.PrimaryKeyConstraint if you want it to be a primary key
        UniqueConstraint('tenant_id', 'id'),
        UniqueConstraint('tenant_id', 'name'),
      )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    label = Column(String, nullable=True)

    additional_info = Column(JSON, nullable=True, default=dict)
    device_data = Column(JSON, nullable=True, default=dict)

    device_profile_id = Column(UUID(as_uuid=True), ForeignKey('device_profiles.id'), nullable=True, index=True)
    customer_id = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=True)
    tenant_id = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=True)
    firmware_id = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=True)
    software_id = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=True)

    device_profile = relationship("DeviceProfile", back_populates="device")
    device_credential = relationship("DeviceCredential", back_populates="device")

    created_at = Column(DateTime(), default=datetime.datetime.now)
    updated_at = Column(DateTime(), onupdate=datetime.datetime.now, default=datetime.datetime.now)


'''
# ThingBoard DataModel
CREATE TABLE IF NOT EXISTS device (
    id uuid NOT NULL CONSTRAINT device_pkey PRIMARY KEY,
    created_time bigint NOT NULL,

    name varchar(255),
    type varchar(255),
    
    label varchar(255),
    additional_info varchar,
    device_data jsonb,
    
    search_text varchar(255),

    device_profile_id uuid NOT NULL,
    customer_id uuid,
    tenant_id uuid,
    firmware_id uuid,
    software_id uuid,
    external_id uuid,

    CONSTRAINT device_name_unq_key UNIQUE (tenant_id, name),
    CONSTRAINT device_external_id_unq_key UNIQUE (tenant_id, external_id),
    CONSTRAINT fk_device_profile FOREIGN KEY (device_profile_id) REFERENCES device_profile(id),
    CONSTRAINT fk_firmware_device FOREIGN KEY (firmware_id) REFERENCES ota_package(id),
    CONSTRAINT fk_software_device FOREIGN KEY (software_id) REFERENCES ota_package(id)
);
'''
