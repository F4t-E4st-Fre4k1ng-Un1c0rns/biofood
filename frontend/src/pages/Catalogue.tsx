import Category from "@/components/Category";
import { useCacheStore } from "@/store/cache";

function Catalogue() {
  const catalogue = useCacheStore();
  return (
    <>
      {catalogue.categories.map((category) => (
        <Category category={category} id={category.id} key={category.id} />
      ))}
    </>
  );
}

export default Catalogue;
