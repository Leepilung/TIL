import React from 'react';
import Categories from '../components/Categories';
import NewsList from '../components/NewsList';
import { useParams } from '../../node_modules/react-router-dom/index';

const NewsPage = () => {
  const params = useParams();
  const category = params.category || 'All';
  console.log(category);

  return (
    <>
      <Categories />
      <NewsList category={category} />
    </>
  );
};

export default NewsPage;
