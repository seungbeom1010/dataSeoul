// 요약
import React from 'react'
import styled from 'styled-components';
// import {VscListUnordered} from 'react-icons/vsc';
import {AiOutlineDollarCircle} from 'react-icons/ai';
import {BsPeople} from 'react-icons/bs';
import {VscBriefcase} from 'react-icons/vsc';
import {BiBuildingHouse} from 'react-icons/bi';
import {BsBarChart} from 'react-icons/bs';
import Map from '../seoulMap';

export default function Summary(props) {
    return (
        <Section id="summary">
                <div className="contentBox">
                    <h2>요약</h2>
                    <p>
                    2021년 12월 1일 대한민국의 코로나 확진자 수는 5,488명이며 서울특별시 누적 코로나 확진자 수는 49,987명입니다. 

                    <br/>
                    <br/>
                    2021년 2분기 기준 서울 특별시의 유동인구는 9억 1,329만명으로 1분기 대비 0.08% 감소된것으로 조사되었습니다. 
                    <br/>
                    <br/>
                    서울특별시의 총 점포수는 26만 7821개소 입니다.
                    2021년 2분기 기준 점포들의 평균매출액은 6893만원이고 평균 영업기간은 115개월이며, 평균 창업률과 폐업률은 각각 2.47%, 2.48%입니다.
                    </p>
                </div>
                <div className="contentMap">
                    <Map/>
                </div>
            <div className="contentList">
                <div className="contentSection">
                    <div className="contentTitle">
                        <AiOutlineDollarCircle/>
                        <h3>매출분석</h3>
                    </div>
                    <ul>
                        <li>매출규모 현황</li>
                        <li>자치구별 매출규모 현황</li>
                        <li>자산, 부채 현황</li>
                    </ul>
                </div>
                <div className="contentSection ">
                    <div className="contentTitle">
                        <BsPeople/>
                        <h3>인구분석</h3>
                    </div>
                    <ul>
                        <li>자산, 부채 현황</li>
                        <li>자산, 부채 현황</li>
                        <li>자산, 부채 현황</li>
                    </ul>
                </div>
                <div className="contentSection">
                    <div className="contentTitle">
                        <VscBriefcase/>
                        <h3>업종분석</h3>
                    </div>
                    <ul>
                        <li>자산, 부채 현황</li>
                        <li>자산, 부채 현황</li>
                        <li>자산, 부채 현황</li>
                    </ul>
                </div>
                <div className="contentSection">
                    <div className="contentTitle">
                        <BiBuildingHouse/>
                        <h3>주변시설</h3>
                    </div>
                    <ul>
                        <li>자산, 부채 현황<p></p></li>
                        <li>자산, 부채 현황</li>
                        <li>자산, 부채 현황</li>
                    </ul>
                </div>
                <div className="contentSection contentSection_end">
                    <div className="contentTitle">
                        <BsBarChart/>
                        <h3>소득소비</h3>                  
                    </div>
                    <ul>
                        <li>자산, 부채 현황</li>
                        <li>자산, 부채 현황</li>
                        <li>자산, 부채 현황</li>
                    </ul>
                </div>
            </div> 
        </Section>
    )
}

const Section = styled.section `
    display: grid;
    height: 100vh;
    background: #141b2e;
    padding: 8rem 4rem 8rem 9rem;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 60% 40%; 
    grid-template-areas:'contentBox contentMap'
                        'contentList contentList';
    .contentBox{
        
            grid-area: contentBox;
            display: flex;
            align-items:flex-start;
            flex-direction: column;
            color: white;
            h2{
                font-size: 3.5rem;
                font-weight: 550;
                letter-spacing: 0.3rem;
                margin-bottom: 1rem;
                }

            p {
                font-size: 1.1rem;
                line-height: 2rem;
                }
        
            }
            .contentMap{
                margin-left:7rem;
                width:100%;
                height:100%;
                grid-area:contentMap;
            }
    .contentList{
        width:100%; 
        margin-top:7rem;
        margin-left:2rem;
        grid-area:contentList;
        .contentSection{
            float:left;
            width:20%;
            color: white;
            .contentTitle{
                width:12rem;
                border-bottom: 2px solid #ffffff;
                text-align: center;
                padding-bottom:1.5rem;
                margin-bottom: 2rem;
                h3{
                    font-size:1.2rem;
                    font-weight:800;
                }
                svg {
                    margin-left:1.8rem;
                    margin-right:0.1rem;
                    float:left;
                    color: #ffffff;
                    font-size: 1.5rem;
                    font-weight: 300;
                    filter: drop-shadow(0.1rem 0.1rem black);
                }

                ul { 
                    list-style-type:square;

                    li{
                        font-size: 1.3rem;
                     }
                }
        
            }    
            ul { 
                margin:0 auto;
                list-style-type:square;
                li{
                    margin-left:18%;
                    font-size: 1.1rem;
                    margin-top:1rem;
                  }
            
            }
        }
    }
    
    @media screen and (min-width: 260px) and (max-width:450px){
        display: none;
        grid-template-columns: 1fr;
        .contentMap{
            svg{
                display: none;
            } 
        }
    }
`;
