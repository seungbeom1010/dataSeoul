import React from 'react'
import styled from 'styled-components';
import { SalesByCityGraph, SalesByQtrGraph } from './Graphs';

export default function Revenue(props) {
    return (
        <Section id="revenue">
            {/* 상단에 전체설명부분 */}
            <div className="analysisTitle">
                <h2>매출분석</h2>
                <p>서울특별시의 2021년 2분기의 매출액은 총 18.46조이고, 직전 분기 대비 8.59% 증가 하였습니다.
                    <br/>
                    2019년 3분기 성장세를 보이던 서울특별시 총 매출 합계는 코로나가 발생한 2020년 1분기 이후 최고점을 회복하지 못하고 있으며 연말 특수가 있어 일반적으로 매출액이 증가하는 2020년 4분기에도 오히려 총매출액이 하락하는 그래프를 보이고 있습니다.
                    2020년 4월 5일 이후로 지급된 1차 재난 지원금의 효과로 2020년 2분기는 동년 1분기 대비 4.7%p 증가한 수치를 기록하였지만 8월에 지급된 2차 재난 지원금은 예상된 정책효과로인해 1차 대비 큰 효과를 거두지 못 한 것으로 보입니다.
                    </p>
            </div>
            {/* 두번째 단에 세부설명부분 */}
            <div className="analysisSubtitle1"><h2>분기별 매출현황</h2></div>
            <div className="analysisSubtitleEx"> 
                <h2>소득 정보 - 가구 기준</h2>
                <div>6,595만원<br/><span>2019년 경상소득(가구 당)</span></div><div>4,433만원<br/><span>2019년 근로소득(가구 당)</span></div>
                <p>2019년 서울특별시의 가구당 경상소득은 6,595만원 입니다. 그 중 근로소득은4,433만원, 사업소득은 1,080만원, 재산소득은 609만원, 이전소득은 473만원으로 나타났습니다.<br/>
                    서울특별시의 2019년 가구당 경상소득은 전년 대비 1.5% 증가 했고 연도별 평균 6.0% 증가 했습니다. 전국 대비 113% 수준으로 전국 증가율 대비 71.4%로 나타납니다.
                    2019년 서울특별시의 가구당 경상소득은 6,595만원 입니다. 그 중 근로소득은 4,433만원,재산소득은 609만원, 이전소득은 473만원으로 나타났습니다.
                    </p>  
            </div>
            {/* 그래프 */}
            <div className="graph1">
                <div>
                    <SalesByQtrGraph cityId={props.cityId} />             
                </div>
            </div>
            <div className="graph2">
                <h2>자치구별 매출현황</h2>
                <div>
                    <SalesByCityGraph />
                </div>
            </div>
        </Section> 
    )
}

const Section = styled.section `
        background: white;
        display:grid;
        height: 160vh;
        padding:8rem 7rem;
        grid-template-columns: 40% 60%;
        grid-template-rows:20% 5% 35% 40%; 
        grid-template-areas:
                            'analysisTitle analysisTitle'
                            'analysisSubtitle1 analysisSubtitle1'
                            'Explanation graph1'
                            'graph2 graph2';
        .analysisTitle{
            grid-area:analysisTitle;

            h2{
               margin-bottom:1rem;
                font-size: 2.5rem;
               
            }
            p{  
                font-size:1.2rem;
                line-height:2.3rem;
            }
       
       
    }
        .analysisSubtitle1{
            grid-area: analysisSubtitle1;
            display: flex;
            justify-content:center;
            h2{
                height:2.5rem;
                padding-left:1rem;
                border-left: 3px solid;
                font-size:1.8rem;
                letter-spacing:0.5rem;
            }
        }

        .analysisSubtitleEx{
            height:80%;
            grid-area:Explanation;
            h2{
                font-size:1.3rem;
                font-weight:700;
            }
            div{
                padding-top:2rem;
                font-size:2rem;
                float:left;
                width:12rem;
                font-weight:500;
                span{
                    font-size:0.9rem;
                    font-weight:1000;
                    
                }
            }
            p{clear:both; 
              padding-top:2rem;
              line-height:2rem;
            }
    
        }
        .graph1{
            grid-area:graph1;
            div{
                width:95%;
                height:100%;
                float:right;            
            }
        }
        .graph2{
            grid-area:graph2;
            div{
                width:100%;
                height:100%;
            }
            h2{ 
                font-weight:550;  
                width:19rem;
                height:2rem;
                font-size:1.8rem;
                padding-left:1rem;
                border-left: 3px solid;
                margin-bottom:2rem;
            }
            div{
                width:100%;
                height:80%;
            }
            
    
        }
        @media screen and (min-width: 260px) and (max-width:450px){
        display: none;
        grid-template-columns: 1fr;}
`;