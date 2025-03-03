import Category from "@/components/Category";
import { useCatalogueStore } from "@/store/catalogue";

export default () => {
  const catalogue = useCatalogueStore();
  return (
    <>
      {catalogue.categories.map((category) => (
        <Category category={category} key={category.id} id={category.id} />
      ))}
    </>
  );
};
