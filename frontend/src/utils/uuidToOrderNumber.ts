export function uuidToOrderNumber(uuid: string) {
  let out = "";
  for (let i = uuid.length - 1; i > 0; i--) {
    if (uuid[i].match(/\d/)) {
      out += uuid[i];
    }
    if (out.length == 4) {
      break;
    }
  }
  return out;
}
