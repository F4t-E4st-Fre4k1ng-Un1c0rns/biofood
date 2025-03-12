import { useAuthStore } from "@/store/auth";

export async function sendSubscription(
  subscription: PushSubscription
): Promise<void> {
  const { getState: getAuthState } = useAuthStore;
  if (!getAuthState().loggedIn) {
    return;
  }

  const pushId = localStorage.getItem("pushId") || undefined;

  const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/push`, {
    method: "POST",
    body: JSON.stringify({
      endpoint: subscription.endpoint,
      p256dh: subscription.toJSON().keys?.p256dh,
      auth: subscription.toJSON().keys?.auth,
      id: pushId,
    }),
    headers: {
      Authorization: `Bearer ${getAuthState().user?.token}`,
      "Content-Type": "application/json",
    },
  });
  const json = await response.json();
  localStorage.setItem("pushId", json.id);
}
