#define what to create
from fastapi import APIRouter

from models.users import User
from config.db import conn
from schemas.users import userEntity, usersEntity
from bson import ObjectId
user=APIRouter()

@user.get('/')
async def find_all_users():
    return usersEntity(conn.local.user.find())

@user.get('/{id}')
async def find_one_user(id):
    return userEntity(conn.local.user.find_one({"_id":ObjectId(id)}))


@user.post('/')
async def create_users(user: User):
    conn.local.user.insert_one(dict(user))
    return usersEntity(conn.local.user.find())


@user.put('/{id}')
async def update_users(id,user: User):
    conn.local.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return userEntity(conn.local.user.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def delete_users(id,user: User):
    return userEntity(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))