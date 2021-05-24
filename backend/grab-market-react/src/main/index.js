import React, { useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import "./index.css";
function MainPage() {
  const [products, setProducts] = React.useState([]);

  React.useEffect(function () {
    //axios는 비동기식을 편하게 사용하기 위한 패키지이다.
    axios
      .get(
        //아래 주소의 값을 (여기엔 JSON이 들어있다.) 가져온다
        "https://31cdbc01-bf29-472e-8e02-97ffabadc851.mock.pstmn.io/products"
      )
      .then(function (result) {
        //호출 성공시 실행한다.
        console.log("then", result);
        console.log("data = ", result.data);
        const products = result.data;
        setProducts(products);
      })
      .catch(function (error) {
        //호출 실패시 실행한다.
        console.log("에러 발생!! ", error);
      });
  }, []);
  if (products.length == 0) return <div>상품 정보를 읽어오는 중 입니다.</div>;

  return (
    <div>
      <main>
        <section>
          <h1 className="blind">메인</h1>
          <div id="main">
            <section>
              <h1 className="blind">베너</h1>
              <div id="banner">
                <div>
                  <img src="./images/banners/banner1.png" alt="배너" />
                </div>
              </div>
            </section>
            <section>
              <h1>판매되는 상품들</h1>
              <div id="product-list">
                {/* loop돌리자! */}
                {products.map(function (product, index) {
                  return (
                    <div className="product-card">
                      <Link
                        className="product-link"
                        to={"/product/" + product.id}
                      >
                        <div>
                          <img className="product-img" src={product.imageUrl} />
                        </div>
                        <div className="product-contents">
                          <span className="product-name">{product.name}</span>
                          <span className="product-price">
                            {product.price}원
                          </span>
                          <div className="product-seller">
                            <img
                              className="product-avatar"
                              src="images/icons/avatar.png"
                              alt="아바타"
                            />
                            <span> {product.seller}</span>
                          </div>
                        </div>
                      </Link>
                    </div>
                  );
                })}
              </div>
            </section>
          </div>
        </section>
      </main>
    </div>
  );
}

export default MainPage;
