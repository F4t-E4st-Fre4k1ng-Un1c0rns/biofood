import { useAuthStore } from "@/store/auth";
import { useNavigate } from "react-router";
import { IDetectedBarcode, Scanner } from "@yudiel/react-qr-scanner";

function ChefLogin() {
  const auth = useAuthStore();
  const navigate = useNavigate();

  const onTokenInput: React.ChangeEventHandler<HTMLInputElement> = (event) => {
    const token = event.target.value;
    auth.loginByToken(token);
    navigate("/src/pos/chef");
  };

  const onScan = (code: IDetectedBarcode[]) => {
    const token = code[0].rawValue;
    auth.loginByToken(token);
    navigate("/src/pos/chef");
  };

  return (
    <div className="p-8 text-center">
      <h1 className="mb-4">Отсканируйте свой QR код</h1>
      <div className="w-full flex justify-center mb-4">
        <Scanner
          components={{
            finder: false,
          }}
          constraints={{
            facingMode: {
              ideal: "user",
            },
          }}
          onError={console.error}
          onScan={onScan}
          styles={{
            container: {
              width: 500,
            },
            finderBorder: 0,
          }}
        />
      </div>
      <div>
        <label htmlFor="token">или введите токен</label>
        <input
          autoFocus
          className="border rounded ml-1"
          id="token"
          onChange={onTokenInput}
          type="text"
        />
      </div>
    </div>
  );
}

export default ChefLogin;
