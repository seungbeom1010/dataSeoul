import React from 'react';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';
import * as RiIcons from 'react-icons/ri';

export const SidebarData = [
  {
    title: '홈',
    path: '/main',
    icon: <AiIcons.AiFillHome />,
    iconClosed: <RiIcons.RiArrowDownSFill />,
    iconOpened: <RiIcons.RiArrowUpSFill />,
  },
  {
    title: '서비스 소개',
    path: '/',
    icon: <IoIcons.IoIosPaper />,
    iconClosed: <RiIcons.RiArrowDownSFill />,
    iconOpened: <RiIcons.RiArrowUpSFill />,
  },
  {
    title: '지역별 상권분석',
    path: '/',
    icon: <FaIcons.FaEnvelopeOpenText />,
    iconClosed: <RiIcons.RiArrowDownSFill />,
    iconOpened: <RiIcons.RiArrowUpSFill />,
    subNav:[
      {
          "title": "종로구",
          "path": "/11110",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "중구",
          "path": "/11140",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "용산구",
          "path": "/11170",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "성동구",
          "path": "/11200",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "광진구",
          "path": "/11215",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "동대문구",
          "path": "/11230",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "중랑구",
          "path": "/11260",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "성북구",
          "path": "/11290",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "강북구",
          "path": "/11305",
          "icon": <IoIcons.IoIosPaper />
      }, 
      {
          "title": "도봉구",
          "path": "/11320",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "노원구",
          "path": "/11350",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "은평구",
          "path": "/11380",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "서대문구",
          "path": "/11410",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "마포구",
          "path": "/11440",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "양천구",
          "path": "/11470",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "강서구",
          "path": "/11500",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "구로구",
          "path": "/11530",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "금천구",
          "path": "/11545",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "영등포구",
          "path": "/11560",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "동작구",
          "path": "/11590",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "관악구",
          "path": "/11620",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "서초구",
          "path": "/11650",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "강남구",
          "path": "/11680",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "송파구",
          "path": "/11710",
          "icon": <IoIcons.IoIosPaper />
      },
      {
          "title": "강동구",
          "path": "/11740",
          "icon": <IoIcons.IoIosPaper />
      }
  ]
  },
  {
    title: '상권분석 지도',
    path: '/',
    icon: <IoIcons.IoMdHelpCircle />
  }
];
