self.addEventListener("push", function (event) {
  console.log("Received a push message", event);

  const title = "New Notification";
  const body = "You have new updates!";
  const icon = "/images/icon.png";
  const tag = "simple-push-demo-notification-tag";

  event.waitUntil(
    self.registration.showNotification(title, {
      body: body,
      icon: icon,
      tag: tag,
    })
  );
});
