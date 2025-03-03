import type { Meta, StoryObj } from "@storybook/react";

import AddToCart from "./index";

const meta: Meta<typeof AddToCart> = {
  component: AddToCart,
};

export default meta;
type Story = StoryObj<typeof AddToCart>;

export const Empty: Story = {
  args: {
    count: 0,
  },
};

export const Filled: Story = {
  args: {
    count: 10,
  },
};
