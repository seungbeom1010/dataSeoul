import React, { useState } from 'react'
import styled from 'styled-components';

import SideBar from './SideBar';

import {VscListUnordered} from 'react-icons/vsc';
import {AiOutlineDollarCircle} from 'react-icons/ai';
import {BsPeople} from 'react-icons/bs';
import {VscBriefcase} from 'react-icons/vsc';
import {BiBuildingHouse} from 'react-icons/bi';
import {BsBarChart} from 'react-icons/bs';
import {Link} from 'react-router-dom';



export default function NavBar() {

    const [navShow, setnavShow] = useState(false); // 상단 네비게이션바 스크롤 동작에 따른 배경색 변화 navShow
    
    window.addEventListener("scroll", () => {
        window.pageYOffset > 0 ? setnavShow(true) : setnavShow(false);
    })
    
    return (
        <Nav navShow={navShow}>
            
            <NavMain /> {/* 상단 네비게이션바 */}
            
            <NavSub  /> {/* 하단 네비게이션바 */}
                                
        </Nav>
    )
}

function NavMain() {
    return(
        <NavBase>
            
            {/* 왼쪽 상단 메뉴버튼 및 사이드바 */}
            <SideBar /> 

            {/* 로고 */}
            <div className="logo">
                <Link to="/">
                    DATA<span>S</span>eoul
                </Link>
            </div>

            {/* space-between을 위한 임의공간 */}
            <div className='rightMenu'></div>
            
        </NavBase>
    )
}

function NavSub() { 

    const [linkShow, setlinkShow] = useState(false); // 상단 네비게이션바 스크롤 동작에 따른 세부분석 네비게이션바 활성화

    window.addEventListener("scroll", () => {
        window.pageYOffset >= 690 ? setlinkShow(true) : setlinkShow(false);
    })

    function NavTo(props) {
        return(
            <li>
                <a href={props.pageUrl}>
                    {props.pageIcon}
                    <h3>{props.pageName}</h3>
                </a>
            </li>
            )
        }

    return(
        <NavActive linkShow={linkShow}>
            <ul>
                <NavTo pageUrl={'#summary'} pageIcon={<VscListUnordered/>} pageName={'요약'} />
                <NavTo pageUrl={'#revenue'} pageIcon={<AiOutlineDollarCircle/>} pageName={'매출분석'} />
                <NavTo pageUrl={'#population'} pageIcon={<BsPeople/>} pageName={'인구분석'} />
                <NavTo pageUrl={'#sector'} pageIcon={<VscBriefcase/>} pageName={'업종분석'} />
                <NavTo pageUrl={'#facility'} pageIcon={<BiBuildingHouse/>} pageName={'주변시설'} />
                <NavTo pageUrl={'#es'} pageIcon={<BsBarChart/>} pageName={'소득/소비'} />
            </ul>
        </NavActive>
    )
}



const Nav = styled.div` // NavBar 전체 
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-direction: column;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 2;
    position: fixed;
    background: ${ ( { navShow } ) => navShow ? "rgba(20, 27, 46, 0.8)":"transparent"};
    padding: 0.5vw;
    
    @media screen and (min-width: 320px) and (max-width:450px){
        grid-template-columns: 1fr;
        padding: 2vw;
    }
`

const NavBase = styled.div` // 기본 네비게이션바
    display: flex;
    justify-content: space-between;
    width: 100%;
    
    .navBar {
        width: 5vw;
        display: flex;
        align-items: center;
        margin-left: 0.5vw;
        .menuBars {
            display: flex;
            justify-content: left;
            align-items: center;
            color: white;
            text-decoration: none;
            gap: 0.3vw;

            svg{
                font-size: 1.3rem;
            }
            h3{
                font-size: 0.7rem;
                font-weight: 300;
            }
            
        }
    }

    .nav-menu {
    background-color: #060b26;
    width: 250px;
    height: 100vh;
    display: flex;
    justify-content: center;
    position: fixed;
    top: 0;
    left: -100%;
    transition: 900ms;
    }

    .nav-menu.active {
    left: 0;
    transition: 350ms;
    }

    .nav-text {
    display: flex;
    justify-content: start;
    align-items: center;
    padding: 8px 0px 8px 16px;
    list-style: none;
    height: 60px;
    }

    .nav-text a {
    text-decoration: none;
    color: #f5f5f5;
    font-size: 18px;
    width: 95%;
    height: 100%;
    display: flex;
    align-items: center;
    padding: 0 16px;
    border-radius: 4px;
    }

    .nav-text a:hover {
    background-color: #1a83ff;
    }

    .nav-menu-items {
    width: 100%;
    span {
    margin-left: 16px;
    }

    }

    .navbar-toggle {
    background-color: #060b26;
    width: 100%;
    height: 80px;
    display: flex;
    justify-content: start;
    align-items: center;
    padding: 2rem;
        .menu-bars{
            svg{
                color: white;
                font-size: 2rem;
            }
        }
    }

    
    .logo{
        a{
            text-decoration: none;
            color: white;
            font-size: 1.3rem;
            font-weight: 400;
        }
        span{
            font-weight: 600;
            color: red;
        }
    }

    @media screen and (min-width: 320px) and (max-width: 425px){
        
    }

    .rightMenu{
        width: 5vw;
        margin-right: 0.5vw;
    }
`

const NavActive = styled.div` // 세부분석 네이게이션바
    width: 100%;
    display: ${ ( { linkShow } ) => linkShow ? "flex":"none"};
    justify-content: center;
    align-items: center;
    flex-direction: column;
    z-index: 2;

    ul {
        width: 100%;
        display: flex;
        justify-content: space-evenly;
        list-style-type: none;
        li {
            a{
                display:flex;
                flex-direction: column;
                color: #c5c5c5;
                text-decoration: none;

                svg {
                    width:100%;
                    font-size: 1.3rem;
                    transition: 0.3s ease-in-out;  
                    margin-bottom: 0.2vw;
                }
                
                h3 {
                    font-size: 0.8rem;
                    font-weight: 500;
                    transition: 0.3s ease-in-out;
                }
                
                &:hover {
                    svg{
                        transform: scale(1.1);
                        color: white;
                    }
                    h3 {
                        transform: scale(1.1);
                        color: white;
                    }
                }
            }
        }
    }

    @media screen and (min-width: 320px) and (max-width: 425px){
        display: none;
    }


        

`