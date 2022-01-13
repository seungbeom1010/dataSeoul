
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';
import { SidebarData } from './SidebarData';
import {HiOutlineMenu} from 'react-icons/hi';


export default function SideBar() {

    const [sidebar, setSidebar] = useState(false);
  
    const showSidebar = () => setSidebar(!sidebar);

    return (
      <>
        {/* 상단 메뉴바 */}
        <NavIcon to='#' onClick={showSidebar}> 
          <HiOutlineMenu />
          <h3>MENU</h3>
        </NavIcon>

        {/* 상단 메뉴바 클릭시 나오는 사이드바 */}
        <SidebarNav sidebar={sidebar}>
          
          <SidebarWrap >
            {SidebarData.map((item, index) => {
              return <SubMenu item={item} key={index} />;
            })}
          </SidebarWrap>

          <div className="sideBarback" onClick={showSidebar}></div>

        </SidebarNav>
      </>

    );
}

const NavIcon = styled(Link)`
  display: flex;
  justify-content: flex-start;
  align-items: center;
  text-decoration: none;
  color: white;
  svg{
    font-size: 1.3rem;
  }

  h3{
      
      font-weight: 300;
      font-size: 0.8rem;
  }
`

const SidebarNav = styled.nav`
  background: rgba(255, 255, 255, 0.5);
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: left;
  position: fixed;
  top: 0;
  left: ${({ sidebar }) => (sidebar ? '0' : '-100%')};
  transition: 350ms;
  z-index: 10;
  .sideBarback{
    height: 100vh;
    width: 40%;
    color: transparent;
  }

`

const SidebarWrap = styled.div`
  background: black;
  padding-top: 5vw;
  width: 250px;
  overflow: scroll;
  ::-webkit-scrollbar{
    display: none;
  }
`


// SidebarData.js로 부터 받은 item
// 
const SubMenu = ({ item }) => {

  const [subNav, setsubNav] = useState(false);
  const showSubnav = () => setsubNav(!subNav);
  
  return (
    <>
      <SidebarLink to={item.path} onClick={item.subNav && showSubnav}>
        
        {/* 사이드바 메인 메뉴 */}
        <div> 
          {item.icon}
          <SidebarLabel>{item.title}</SidebarLabel>
        </div>
        
        {/* 서브메뉴 있을 시 옆에 화살표 아이콘 표시 */}
        <div>
          {item.subNav && subNav
            ? item.iconOpened
            : item.subNav
            ? item.iconClosed
            : null
          }
        </div>
      </SidebarLink>
      
      {/* 사이드바 서브메뉴 */}
      {subNav && item.subNav.map((item, index) => {
          return (
            <DropdownLink to={item.path} key={index}>
              {item.icon}
              <SidebarLabel>{item.title}</SidebarLabel>
            </DropdownLink>
            )
          }
        )
      }
    </>
  );
}

const SidebarLink = styled(Link)`
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #ffffff;
  list-style: none;
  text-decoration: none;
  
  padding: 20px;
  height: 50px;
  font-size: 1rem;

  &:hover {
    background: #252831;
    border-left: 4px solid #632ce4;
    cursor: pointer;
  }
`

const SidebarLabel = styled.span`
  margin-left: 16px;
`

const DropdownLink = styled(Link)`
  background: #414757;
  height: 50px;
  padding-left: 3rem;
  display: flex;
  align-items: center;
  text-decoration: none;
  color: #f5f5f5;
  font-size: 1.1rem;
  font-weight: 300;

  &:hover {
    background: #632ce4;
    cursor: pointer;
  }
`






