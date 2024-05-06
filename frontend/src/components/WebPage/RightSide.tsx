import React from 'react';
import MainCanvas from '../Star/MainCanvas';
import * as r from '../style/WebPageStyle';

const RightSide = () => {
  return (
    <r.RightWrapper>
      <r.CanvasContainer>
        <div className="card">
          <div className="content">
            <div className="back">
              <div className="back-content">
                <MainCanvas />
              </div>
            </div>
          </div>
        </div>
      </r.CanvasContainer>
    </r.RightWrapper>
  );
};

export default RightSide;

