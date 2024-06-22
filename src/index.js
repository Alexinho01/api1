import { Elysia } from "elysia";
import { registrar } from "./endpoints/registrar";
import { bloquear } from "./endpoints/bloquear";
import { informacion } from "./endpoints/informacion";
import { verificar } from "./endpoints/verificar";

const app = new Elysia()
  .get("/", async () => {
    return "MAIN"
  })
  .use(registrar)
  .use(bloquear)
  .use(informacion)
  .use(verificar)
  .listen(3000);

console.log(
  `🦊 Elysia is running at ${app.server?.hostname}:${app.server?.port}`
);
