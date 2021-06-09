import React from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import "./index.css";
import { API_URL } from "../constants";
//시간 표현
import dayjs from "dayjs";
import "dayjs/locale/ko";
import relativeTime from "dayjs/plugin/relativeTime";
dayjs.extend(relativeTime);
dayjs.locale("ko");

function ProductPage() {
  const { id } = useParams();
  const [product, setProducts] = React.useState([]);

  React.useEffect(function () {
    axios
      .get(
        `${API_URL}/grab/${id}/`
        // "https://31cdbc01-bf29-472e-8e02-97ffabadc851.mock.pstmn.io/products/" + id
      )
      .then(function (result) {
        console.log(result);
        const product = result.data;
        setProducts(product);
      })
      .catch(function (error) {
        console.log("에러 발생 : " + error);
      });
  }, []);
  if (product.length === null) {
    return <h1>상품 정보를 받고 있습니다.</h1>;
  }
  console.log(product.ImageUrl);
  return (
    <div>
      <div id="image-box">
        <img src={`${API_URL}/${product.ImageUrl}`} />
      </div>
      <div id="profile-box">
        <img src="/images/icons/avatar.png" />
        <span>{product.seller}</span>
      </div>
      <div id="contents-box">
        <div id="name">{product.name}</div>
        <div id="price">{product.price}</div>
        <div id="creatAt">{dayjs(product.createAt).fromNow()}</div>
        <div id="description">{product.description}</div>
      </div>
    </div>
  );
}
export default ProductPage;
