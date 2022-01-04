import React from 'react'
import styled from 'styled-components';

export default function Footer() {
    return (
        <div className="footer">
            <Section id = 'footer'>
                <div className="about">
                    <div className="title"> 
                    {/* footer content 보류 */}
                        {/* <h3>About Us</h3> */}
                    </div>
                    <p>
                    </p>
                </div>
                <div className="contact">
                    <div className="title">
                        <h3>Contact Us</h3>
                    </div>
                    <div class="contact info">
                        <p>이어드림 프로젝트</p>
                        <p>주소 : 서울특별시 마포구 양화로 186 스파크플러스 6층</p>
                    </div>
                    <h2>
                    Copyright &copy; 2021 DATA<span>S</span>eoul
                    </h2>
                </div>
            </Section>
            <Mobile>
                <a href="https://yeardream.lms.elice.io/home">CONTACT US</a>
                <div className="info">
                    <h3>이어드림 프로젝트</h3>
                    <h3>서울특별시 마포구 양화로 186 스파크플러스 6층</h3>
                </div>
                <h2>COPYRIGHT &copy;DATASeoul</h2>
                <h2>ALL RIGHTS RESERVED</h2>
            </Mobile>
        </div>
    )
}

// 웹브라우져용
const Section = styled.footer `
    margin: 0;
    background: #141b2e;
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: top;
    width: 100%;
    padding: 2.5vw;
    .about {
        display: flex;
        flex-direction: column;
        width: 50%;
    }
    
    .about .title {
        font-size: 1.2rem;
        margin-bottom: 0.8vw;
    }

    .about p {
        font-size: 1rem;
        font-weight: 300;
        margin-bottom: 2vw;
    }

    .contact {
        display: flex;
        justify-content: right;
        flex-direction: column;
        .title{
            font-size: 1.2rem;
            margin-bottom: 0.5vw;
        }
        p{
            font-size: 1rem;
            font-weight: 300;
            margin-bottom: 0.5vw;
        }
        .info {
            margin-bottom: 1.5vw;
        }

        h2 {
            text-align: right;
            font-size: 1rem;
            span{
                color: red;
            }
        }
    }

    @media screen and (min-width: 320px) and (max-width:450px){
        display: none;
        grid-template-columns: 1fr;
            
        }
`;

// 모바일용
const Mobile = styled.footer `
    display: none;

    @media screen and (min-width: 320px) and (max-width:450px) {
        display: flex;
        width: 100%;
        grid-template-columns: 1fr;
        background: #141b2e;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding-bottom: 5vw;
        color: white;
        a{
            font-size: 1rem;
            border: 1px solid white;
            padding: 0.5rem;
            margin-bottom: 2vh;
            text-decoration: none;
            color: white;
        }
        .info{
            display: flex;
            align-items: center;
            flex-direction: column;
            margin-bottom: 1.5vh;
            h3{
            font-size: 0.8rem;
            font-weight: 400;
            padding: 0.5vh;
            }
        }        
        h2{
            font-size: 0.7rem;
            font-weight: 300;
            padding-bottom: 1vw;
        }
    }
`