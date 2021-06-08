import React from "react";
import {
  Form,
  Divider,
  Input,
  InputNumber,
  Button,
  Upload,
  message,
} from "antd";
import "./index.css";
import { API_URL } from "../constants";
import axios from "axios";
import { useState } from "react";
import { useHistory } from "react-router-dom";
import { FormOutlined } from "@ant-design/icons";

function UploadPage() {
  //useState : 값이 변경되면 refrash해준다.
  const [imageUrl, setImageUrl] = useState(null);
  const history = useHistory();
  const onSubmit = (values) => {
    let form = new FormData();
    form.append("name", values.name);
    form.append("seller", values.seller);
    form.append("price", values.price);
    form.append("description", values.description);
    form.append("ImageUrl", imageUrl);
    console.log("submit : image" + imageUrl);
    // 어플리케이션 서버 호출 !!
    axios
      .post(`${API_URL}/grab/`, form)
      .then((result) => {
        console.log(result);
        // replace를 하지 않는다면 무한 등록이 된다.
        // (데이터는 그대로 있고, 전송을 계속하니 당연!)
        message.success("전송 완료!");
        history.replace("/");
      })
      .catch((error) => {
        console.log(error);
        //message 는 andD를 import 해야 사용 가능!
        message.error(`에러 발생! ${error.message}`);
      });
  };
  const onChangeImage = (values) => {
    console.log(values);
    // 업로드 완료시
    if (values.file.status === "uploading") {
      return;
    }
    //파일 업로드 완료시
    if (values.file.status === "done") {
      const response = values.file.response;
      //백앤드의 ImageUrl로 접근
      const imageUrl = response.ImageUrl;
      console.log("done Img: " + response.ImageUrl);
      setImageUrl(imageUrl);
      message.success("파일 업로드 완료");
    }
  };

  return (
    <div id="upload-container">
      {/* onFinish : Form이 끝나면 onSubmit을 실행한다. */}
      <Form name="상품 업로드" onFinish={onSubmit}>
        <Form.Item
          name="upload"
          label={<div className="upload_label">상품사진</div>}
        >
          <Upload
            name="image"
            action={`${API_URL}/image/`}
            listType="picture"
            showUploadList={false}
            onChange={onChangeImage}
          >
            {imageUrl ? (
              <img src={`${API_URL}/${imageUrl}`} />
            ) : (
              <div id="upload-img-placeholder">
                <img src="/images/icons/camera.png" />
                <span>이미지를 업로드해주세요.</span>
              </div>
            )}
          </Upload>
        </Form.Item>
        <Divider />
        <Form.Item
          label={<div className="upload-label">판매자 명</div>}
          name="seller"
          rules={[{ required: true, message: "판매자 이름을 입력해주세요." }]}
        >
          <Input
            className="upload-name"
            size="large"
            placeholder="이름을 입력해주세요."
          />
        </Form.Item>
        <Divider />
        <Form.Item
          label={<div className="upload-label">상품 이름</div>}
          name="name"
          rules={[{ required: true, message: "상품 이름을 입력해주세요." }]}
        >
          <Input
            className="upload-name"
            size="large"
            placeholder="상품 이름을 입력해주세요."
          />
        </Form.Item>
        <Divider />
        <Form.Item
          label={<div className="upload-label">상품 가격</div>}
          name="price"
          rules={[{ required: true, message: "상품 가격을 입력해주세요." }]}
        >
          <InputNumber defaultValue={0} className="upload-price" size="large" />
        </Form.Item>
        <Divider />
        <Form.Item
          label={<div className="upload-label">상품 소개</div>}
          name="description"
          rules={[{ required: true, message: "상품 소개를 입력해주세요." }]}
        >
          <Input.TextArea
            size="large"
            id="product-description"
            showCount
            maxLength={300}
            placeholder="상품 소개를 입력해주세요."
          />
        </Form.Item>
        <Form.Item>
          <Button id="submit-buttion" size="large" htmlType="submit">
            상품 등록
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
}
export default UploadPage;
