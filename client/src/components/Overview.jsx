import React from 'react'
import styled from 'styled-components';
import mainSeoul from '../assets/images/mainSeoul.jpg';
import {VscListUnordered} from 'react-icons/vsc';
import {AiOutlineDollarCircle} from 'react-icons/ai';
import {BsPeople} from 'react-icons/bs';
import {VscBriefcase} from 'react-icons/vsc';
import {BiBuildingHouse} from 'react-icons/bi';
import {BsBarChart} from 'react-icons/bs';
import cityData from '../assets/data/data.json';


export default function Overview(props) {

    const cityId = parseInt(props.cityId, 10) || 1;
    const cityInfo = cityData.find(cityInfo => (
        cityInfo.id === cityId
    ));
    
    return (
        <Section>
            {/* districtName: 메인페이지 도시이름 */}           
            <div className="districtName">
                <h2 key={cityInfo.id}>
                    {cityInfo.title}
                </h2>
            </div>
            
            {/* districtTable: 메인페이지 도시별 요약현황 */}
            <div className="districtTable">
                <div className="Table">
                    <div className="column">
                        <h3>유동인구</h3>
                        <p>{new Intl.NumberFormat().format(Math.floor(cityInfo.content[0] / 1000000))}백만명</p>
                    </div>
                    <div className="column">
                        <h3>평균매출액</h3>
                        <p>{new Intl.NumberFormat().format(Math.floor(cityInfo.content[1] / 1000000))}백만원</p>
                    </div>
                    <div className="column">
                        <h3>코로나</h3>
                        <p>{new Intl.NumberFormat().format(cityInfo.content[2])}명</p>
                    </div>
                </div>
                <div className="Table">
                    <div className="column">
                        <h3>점포수</h3>
                        <p>{new Intl.NumberFormat().format(cityInfo.content[3])}개</p>
                    </div>
                    <div className="column">
                        <h3>펑균영업기간</h3>
                        <p>{new Intl.NumberFormat().format(Math.floor(cityInfo.content[4]))}개월</p>
                    </div>
                    <div className="column">
                        <h3>창업/폐업률</h3>
                        <p><span>{new Intl.NumberFormat('ko', {maximumFractionDigits: 2}).format(cityInfo.content[5])}/{new Intl.NumberFormat('ko', {maximumFractionDigits: 2}).format(cityInfo.content[6])}</span>%</p>
                    </div>
                </div>
            </div>
            {/* linkTodetail: 메인페이지 세부 분석 navigation bar */}
            <div className="linkTodetail">
                <ul>
                    <li>
                        <a href="#summary">
                            <VscListUnordered/>
                            <h3>요약</h3>
                        </a>
                    </li>
                    <li>
                        <a href="#revenue">
                            <AiOutlineDollarCircle/>
                            <h3>매출분석</h3>
                        </a>
                    </li>
                    <li>
                        <a href="#population">
                            <BsPeople/>
                            <h3>인구분석</h3>
                        </a>
                    </li>
                    <li>
                        <a href="#sector">
                            <VscBriefcase/>
                            <h3>업종분석</h3>  
                        </a>
                    </li>
                    <li>
                        <a href="#facility">
                            <BiBuildingHouse/>
                            <h3>주변시설</h3>  
                        </a>
                    </li>
                    <li>
                        <a href="#es">
                            <BsBarChart/>
                            <h3>소득/소비</h3>  
                        </a>
                    </li>
                </ul>
            </div>
        </Section>
    )
}

const Section = styled.section `
    display: grid;
    grid-template-areas: 'districtName'
                        'districtTable'
                        'linkTodetail';

    grid-template-columns: 1fr;
    grid-template-rows: 1fr 1fr 1fr;
    height: 100vh;

    background: linear-gradient(
        to bottom, 
        rgba(20, 27, 46, 0) 0%,
        rgba(20, 27, 46, 0.3) 25%,
        rgba(20, 27, 46, 0.5) 40%,
        rgba(20, 27, 46, 0.7) 50%,
        rgba(20, 27, 46, 1) 95%, 
        rgba(20, 27, 46, 1) 100%), 
        url(${mainSeoul});

    background-size: cover;

    background-position: center;

    color: white;
    
    .districtName{
        grid-area: districtName;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 17vh;

        h2 {
            font-size: 5rem;
            font-weight: 400;
            text-shadow: 0.2rem 0.2rem black;
            letter-spacing: 1.5rem;
            color:#f2f2f2; 
        }
    }

    .districtTable{
        contain: inline-size;
        grid-area: districtTable;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        margin-top: 10vh;

        .Table{
            width: 40%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            text-shadow: 0.2rem 0.2rem black;
            padding: 2rem;

            .column{
                
                width: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;

                h3{
                    color:#C0C0C0; 
                    font-size: 1.rem;
                    font-weight: 400;
                    margin-bottom: 0.5rem; 
                }

                p{
                    font-size: 2.2rem;

                    span{
                        font-size: 2.4rem;
                    }
                }
            }
        }
    }
    
    .linkTodetail{
        /* contain: style layout inline-size; */
        grid-area: linkTodetail;
        display: flex;
        justify-content: center;
        align-items: center;
        padding-bottom: 8vh;

        ul {
            display: flex;
            list-style-type: none;
            gap: 7vw;

            li {

                a{
                    display:flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    color: #c5c5c5;
                    text-decoration: none;

                    svg {
                        width:100%;
                        font-size: 2rem;
                        transition: 0.3s ease-in-out;  
                        margin-bottom: 0.3vw;
                    }

                    h3 {
                        font-size: 1rem;
                        font-weight: 400;
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
    }


    /* @container (min-witdh: 320px) and (max-width:350) {
            .districtTable {
                font-size: 15px;
            }
    } */

    @media screen and (min-width: 320px) and (max-width: 425px){
        display: grid;
        grid-template-columns: 1fr;
        width: 100%;
        background: linear-gradient(
        to bottom, 
        rgba(20, 27, 46, 0) 0%,
        rgba(20, 27, 46, 0) 25%,
        rgba(20, 27, 46, 0.3) 40%,
        rgba(20, 27, 46, 0.5) 50%,
        rgba(20, 27, 46, 0.6) 95%, 
        rgba(20, 27, 46, 1) 100%), 
        url(${mainSeoul});
        
        background-size: cover;
        background-position: center;

        .districtName{
            h2{
                font-size: 3rem;
                letter-spacing: 0;
            }
        }

        .districtTable{
            display: flex;
            margin: 0;
            padding: 0;
             .Table{
                 width: 100%;
                 .column{
                    h3 {
                        color: white;
                        font-size: 1rem;
                    }

                    p{
                        font-size: 1.2rem;

                        span{
                            font-size: 1rem;
                        }
                    }
                }
            }
        }
        
        .linkTodetail{
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0;
            ul {
                gap: 1vw;
                li{
                    a{
                        h3{
                            font-size: 0.8rem;
                        }
                    }
                }
            }
        }
    }
`