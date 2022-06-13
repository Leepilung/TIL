import React from 'react';
import styled from 'styled-components';

const NewsItemBlock = styled.div`
  display: flex;

  .thumbnail {
    margin-left: 1rem;
    img {
      display: block;
      width: 160px;
      height: 100px;
      object-fit: cover; // img나 video등의 대체 요소의 컨텐츠 크기를 어떻게 조절할 지 지정하는 속성
      // cover의 경우 요소를 박스 가득 채운다. 그러나 가로세로 일치 하지 않으면 잘라먹는다.
    }
  }

  .content {
    h2 {
      margin: 0;
      a {
        color: black;
      }
    }
    p {
      margin: 0;
      line-height: 1.5;
      margin-top: 0.5rem;
      white-space: normal; // 스페이스, 탭, 줄바꿈, 자동 줄바꿈을 어떻게 처리할지 정하는 속성
    }
  }
  & + & {
    margin-top: 3rem;
  }
`;

const NewsItem = ({ article }) => {
  const { title, description, url, urlToImage } = article;
  return (
    <NewsItemBlock>
      {urlToImage && (
        <div className="thumbnail">
          <a href={url} target="_blank" rel="noopener noreferrer">
            {/* a태그의 target _blank는 연결 문석를 새창으로 여는 속성 */}
            <img src={urlToImage} alt="thumbnail" />
          </a>
        </div>
      )}
      <div className="contents">
        <h2>
          <a href={url} target="_blank" rel="noopener noreferrer">
            {/* a태그의 rel 속성 링크 : http://www.tcpschool.com/html-tag-attrs/a-rel */}
            {title}
          </a>
        </h2>
        <p>{description}</p>
      </div>
    </NewsItemBlock>
  );
};

export default NewsItem;
