import { Elysia } from "elysia";
import { registrar } from "./endpoints/registrar";

const app = new Elysia()
  .get("/", async () => {
    return "MAIN"
  })
  .use(registrar)
  .listen(3000);

console.log(
  `🦊 Elysia is running at ${app.server?.hostname}:${app.server?.port}`
);
