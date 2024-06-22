import { Elysia } from "elysia";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export const desmarcarCorreo = new Elysia()
    .delete("api/desmarcarcorreo", async ({body}) => {
        try{
            const usuario = await prisma.usuario.findUnique({
                where: {
                    direccion_correo: body.correo
                }
            })
            if (usuario == null){
                return {
                    "estado": 200,
                    "mensaje": "No existe el usuario"
                }
            }

            if (usuario.password == body.clave){
                
                const favoritoDesmarcar = await prisma.favorito.findUnique({
                    where:{
                        id_usuario_favorito: body.id_correo_favorito
                    }
                })

                if(favoritoDesmarcar != null){

                    await prisma.favorito.delete({
                        where:  {
                            id_usuario_favorito: favoritoDesmarcar.id_usuario_favorito
                        }
                    })
                    console.log(body.correo + "ha eliminado la id favorita" + favoritoDesmarcar.id_favorito)
                }
                else{
                    return{
                        "estado": 400,
                        "mensaje": "No existe el correo a desmarcar"
                    }
                }
            }

        }catch(error){
            console.log(error)
            return{
                "estado": 400,
                "mensaje": "No se ha podido eliminar el Favorito"
            }
        }})
