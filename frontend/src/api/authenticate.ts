import User from "@/types/User";

export async function load(token: string): Promise<User> {
  if (import.meta.env.VITE_MOCK_API) {
    throw new Error();
  }

  const response = await fetch(
    `${import.meta.env.VITE_API_BASE_URL}/authenticate`,
    {
      method: "POST",
      body: JSON.stringify({
        oauthToken: token,
        oauthMethod: "yandexId",
      }),
      headers: {
        "Content-Type": "application/json",
      },
    }
  );
  const json = await response.json();
  const user = {
    role: json.user.role,
    email: json.user.email,
    token: json.accessToken,
  };
  return user;
}
