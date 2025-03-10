export function uuidToOrderNumber(uuid: string) {
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
