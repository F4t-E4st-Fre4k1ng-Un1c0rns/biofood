import { sendSubscription } from "@/api/push";

export function subscribeUserToPush() {
  return navigator.serviceWorker
    .register("/serviceWorker.js")
    .then(function (registration) {
      const subscribeOptions = {
        userVisibleOnly: true,
        applicationServerKey: import.meta.env.VITE_PUBLIC_VAPID_KEY,
      };

      return registration.pushManager.subscribe(subscribeOptions);
    })
    .then(function (pushSubscription) {
      console.log(
        "Received PushSubscription: ",
        JSON.stringify(pushSubscription)
      );
      sendSubscription(pushSubscription);
      return pushSubscription;
    });
}
