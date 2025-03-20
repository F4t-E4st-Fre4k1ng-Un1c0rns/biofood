function uuidToOrderNumber(uuid) {
  let out = "";
  for (let index = uuid.length - 1; index > 0; index--) {
    if (uuid[index].match(/\d/u)) {
      out += uuid[index];
    }
    if (out.length === 4) {
      break;
    }
  }
  return out;
}

self.addEventListener("push", function (event) {
  const order = JSON.parse(event.data.text());
  const orderId = uuidToOrderNumber(order.id);
  const title = `Заказ №${orderId} ${order.status === "ready" ? "готов к выдаче" : "отклонен"}`;

  event.waitUntil(self.registration.showNotification(title));
});
