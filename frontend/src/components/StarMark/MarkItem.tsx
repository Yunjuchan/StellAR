import React, { useState } from 'react';
import * as m from '../style/StarMarkStyle';
import { useMutation } from '@tanstack/react-query';
import { DeleteStarMark } from '../../apis/StarMarkApis';
import useUserStore from '../../stores/userStore';
import useStarStore from '../../stores/starStore';

type Props = {
  starId: string;
  bookmarkName: string;
  createTime: string;
};

const MarkItem = ({ starId, bookmarkName, createTime }: Props) => {
  const [isSaved, setIsSaved] = useState(true);
  const { userId } = useUserStore();
  const starStore = useStarStore();
  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('ko-KR', {
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
    });
  };

  const handleCheckBox = (event: React.ChangeEvent<HTMLInputElement>) => {
    setIsSaved(!isSaved);
    mutate({ userId, starId });
  };

  const { mutate } = useMutation({
    mutationFn: DeleteStarMark,
    onSuccess(result: string) {
      console.log(result);
      starStore.setMarkSaveToggle(!starStore.markSaveToggle);
    },
  });

  return (
    <>
      <m.StarInfo>
        <m.NameBox>
          <m.BookMarkName>{bookmarkName}</m.BookMarkName>
          <m.StarName>{starId}</m.StarName>
        </m.NameBox>
        <m.Date>{formatDate(createTime)}</m.Date>
        <m.Star>
          <label className="container">
            <input
              type="checkbox"
              checked={isSaved}
              onChange={handleCheckBox}
            />
            <svg
              id="Layer_1"
              version="1.2"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <g>
                <g>
                  <path d="M9.362,9.158c0,0-3.16,0.35-5.268,0.584c-0.19,0.023-0.358,0.15-0.421,0.343s0,0.394,0.14,0.521    c1.566,1.429,3.919,3.569,3.919,3.569c-0.002,0-0.646,3.113-1.074,5.19c-0.036,0.188,0.032,0.387,0.196,0.506    c0.163,0.119,0.373,0.121,0.538,0.028c1.844-1.048,4.606-2.624,4.606-2.624s2.763,1.576,4.604,2.625    c0.168,0.092,0.378,0.09,0.541-0.029c0.164-0.119,0.232-0.318,0.195-0.505c-0.428-2.078-1.071-5.191-1.071-5.191    s2.353-2.14,3.919-3.566c0.14-0.131,0.202-0.332,0.14-0.524s-0.23-0.319-0.42-0.341c-2.108-0.236-5.269-0.586-5.269-0.586    s-1.31-2.898-2.183-4.83c-0.082-0.173-0.254-0.294-0.456-0.294s-0.375,0.122-0.453,0.294C10.671,6.26,9.362,9.158,9.362,9.158z"></path>
                </g>
              </g>
            </svg>
          </label>
        </m.Star>
      </m.StarInfo>
    </>
  );
};

export default MarkItem;
