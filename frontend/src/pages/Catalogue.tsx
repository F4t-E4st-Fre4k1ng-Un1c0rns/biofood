import Category from "@/components/Category";
import { useCacheStore } from "@/store/cache";

export default () => {
  const catalogue = useCacheStore();
  return (
    <>
      {catalogue.categories.map((category) => (
        <Category category={category} key={category.id} id={category.id} />
      ))}
    </>
  );
};
