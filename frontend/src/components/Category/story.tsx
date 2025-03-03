import type { Meta, StoryObj } from "@storybook/react";

import Category from "./index";

const meta: Meta<typeof Category> = {
  component: Category,
};

export default meta;
type Story = StoryObj<typeof Category>;

export const NotLoaded: Story = {
  args: {
    category: {
      id: "1",
      name: "Категория с едой",
      loaded: false,
      dishes: [],
    },
  },
};

export const Loaded: Story = {
  args: {
    category: {
      id: "1",
      name: "Категория с едой",
      loaded: true,
      dishes: [],
    },
  },
};
