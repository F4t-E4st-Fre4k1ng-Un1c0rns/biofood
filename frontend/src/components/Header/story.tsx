import type { Meta, StoryObj } from "@storybook/react";

import Header from "./index";
import { HashRouter } from "react-router";

const component = ({ categories }: Parameters<typeof Header>[0]) => {
  return (
    <HashRouter>
      <Header categories={categories} />
    </HashRouter>
  );
};

const meta: Meta<typeof Header> = {
  component,
};

export default meta;
type Story = StoryObj<typeof Header>;

export const FirstStory: Story = {
  args: {
    categories: [
      {
        id: "1",
        name: "Завтраки",
      },
      {
        id: "2",
        name: "Салаты",
      },
      {
        id: "3",
        name: "Супы",
      },
      {
        id: "4",
        name: "Вторые блюда",
      },
    ],
  },
};
