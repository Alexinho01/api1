import {Elysia} from "elysia";
import {PrismaClient} from "@prisma/client"

export const bloquear = new Elysia()
const usuario = {
    id: 0,
    nombre: '',
};

const prisma = new PrismaClient({
    log: ['info', 'warn', 'error'] 
});

const app2 = new Elysia().decorate('db', prisma);

app2.get('/posts', async ({ db }) => {
    return await db.post.findMany();
});

app2.post('/posts', async ({ db, body }) => {
    return await db.post.create({
        data: body 
    });
});