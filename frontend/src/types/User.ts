export type Roles = "client" | "staff" | "admin" | null;

export default interface User {
  role: Roles;
  token: string | null;
  email: string | null;
}
