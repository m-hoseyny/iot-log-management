from typing import TYPE_CHECKING
import uuid, datetime

from sqlalchemy import Boolean, Column, Integer, String, JSON, UniqueConstraint, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class DeviceProfile(Base):
    __tablename__ = 'device_profiles'
    __table_args__ = (
        # this can be db.PrimaryKeyConstraint if you want it to be a primary key
        UniqueConstraint('provision_device_key'),
      )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    image = Column(String, nullable=True)
    transport_type = Column(String, nullable=True)
    provision_type = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    is_default = Column(Boolean(), default=True)
    profile_data = Column(JSON, nullable=True, default=dict)

    default_rule_chain_id = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False)
    default_dashboard_id = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False)
    default_queue_name = Column(String, nullable=True)
    provision_device_key = Column(String, nullable=True)
    external_id = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False)

    device = relationship("Device", back_populates="device_profile")

    created_at = Column(DateTime(), default=datetime.datetime.now)
    updated_at = Column(DateTime(), onupdate=datetime.datetime.now)


'''CREATE TABLE IF NOT EXISTS device_profile (
    id uuid NOT NULL CONSTRAINT device_profile_pkey PRIMARY KEY,
    created_time bigint NOT NULL,
    name varchar(255),
    type varchar(255),
    image varchar(1000000),
    transport_type varchar(255),
    provision_type varchar(255),
    profile_data jsonb,
    description varchar,
    search_text varchar(255),
    is_default boolean,
    tenant_id uuid, #IGNORE
    firmware_id uuid, #IGNORE
    software_id uuid, #IGNORE
    default_rule_chain_id uuid,
    default_dashboard_id uuid,
    default_queue_name varchar(255),
    provision_device_key varchar,
    external_id uuid,
    CONSTRAINT device_profile_name_unq_key UNIQUE (tenant_id, name),
    CONSTRAINT device_provision_key_unq_key UNIQUE (provision_device_key),
    CONSTRAINT device_profile_external_id_unq_key UNIQUE (tenant_id, external_id),
    CONSTRAINT fk_default_rule_chain_device_profile FOREIGN KEY (default_rule_chain_id) REFERENCES rule_chain(id),
    CONSTRAINT fk_default_dashboard_device_profile FOREIGN KEY (default_dashboard_id) REFERENCES dashboard(id),
    CONSTRAINT fk_firmware_device_profile FOREIGN KEY (firmware_id) REFERENCES ota_package(id),
    CONSTRAINT fk_software_device_profile FOREIGN KEY (software_id) REFERENCES ota_package(id)
);'''