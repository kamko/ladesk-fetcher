from sqlalchemy import create_engine, Column, DateTime, Text, ForeignKey, Table, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

tags_conversations = Table(
    'conversations_tags', Base.metadata,
    Column('conversation_id', Text, primary_key=True),# ForeignKey('helpdesk.conversations.id')), - pouzivaju tagy ktore niesu v tags...
    Column('tag_id', Text, primary_key=True),# ForeignKey('helpdesk.tags.id')),
    schema='helpdesk'
    )

class Tag(Base):
    __tablename__ = 'tags'
    __table_args__ = {'schema': 'helpdesk'}

    id = Column(Text, primary_key=True)
    name = Column(Text)

class Conversation(Base):
    __tablename__ = 'conversations'
    __table_args__ = {'schema': 'helpdesk'}

    id = Column(Text, primary_key=True)
    department_id = Column(Text, ForeignKey('helpdesk.departments.id'))
    status = Column(Text)
    channel_type = Column(Text)
    date_created = Column(DateTime)
    date_changed = Column(DateTime)
    date_due = Column(DateTime)
    owner_name = Column(Text)
    owner_email = Column(Text)
    subject = Column(Text)
    
class MessageGroup(Base):
    __tablename__ = 'messages_groups'
    __table_args__ = {'schema': 'helpdesk'}

    id = Column(Text, primary_key=Table)
    user_id = Column(Text) # nie FK pretoze user != customer
    rtype = Column(Text)
    rstatus = Column(Text)
    date_created = Column(DateTime)
    date_finished = Column(DateTime)
    conversation_id = Column(Text, ForeignKey('helpdesk.conversations.id'))

class Message(Base):
    __tablename__ = 'messages'
    __table_args__ = {'schema': 'helpdesk'}

    id = Column(Text, primary_key=True)
    user_id = Column(Text) #nie FK pretoze user != customer
    rtype = Column(Text)
    date_created = Column(DateTime)
    message_text = Column(Text)
    message_group_id = Column(Text, ForeignKey('helpdesk.messages_groups.id'))
                
class Customer(Base):
    __tablename__ = "customers"
    __table_args__ = {'schema': 'helpdesk'}

    contact_id = Column(Text, primary_key=Text)
    user_id = Column(Text)
    email = Column(Text)
    date_created = Column(DateTime)
    role = Column(String(1))
    gender = Column(String(1))

class Department(Base):
    __tablename__ = "departments"
    __table_args__ = {'schema': 'helpdesk'}
    
    id = Column(Text, primary_key=Text)
    name = Column(Text)
    description = Column(Text)
    #online status netreba :)
    preset_status = Column(Text)
