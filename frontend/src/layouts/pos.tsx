import { Outlet } from "react-router";

export default () => {
  document
    .querySelector("meta[name=viewport]")
    ?.setAttribute(
      "view",
      "width=device-width, initial-scale=1, user-scalable=0"
    );
  return (
    <>
      <div className="select-none">
        <Outlet />
      </div>
    </>
  );
};
