interface Props {
  readonly isDrawerOpen: boolean;
  handleDrawerClose(): void;
}

function Overlay({ isDrawerOpen, handleDrawerClose }: Props) {
  return (
    <>
      <div
        aria-hidden="true"
        className={`fixed bottom-0 left-0 right-0 top-0 bg-gray-500
        ease-in-out duration-300
        ${isDrawerOpen ? "z-0 opacity-30" : "-z-1 opacity-0 pointer-events-none"}`}
        onClick={handleDrawerClose}
      />
    </>
  );
}

export default Overlay;
