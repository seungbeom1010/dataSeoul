import React, {useState} from 'react'
import styled from 'styled-components';
import {FiArrowUp} from 'react-icons/fi';

export default function ScrollToTop() {
    const [scrollState, setScrollState] = useState(false);
    
    const toTop = () => {
        window.scrollTo({ top: 0 });
    };
    
    window.addEventListener("scroll", () => {
        window.pageYOffset > 200 ? setScrollState(true) : setScrollState(false);
    })

    return (
        <ToTop onClick={toTop} scrollState={scrollState}>
            <FiArrowUp />
        </ToTop>
    )
}
  
const ToTop = styled.div `
    display: ${ ( {scrollState} ) => scrollState ? "block":"none" };
    position: fixed;
    cursor: pointer;
    z-index: 10;
    bottom: 1rem;
    right: 1.3rem;
    background: rgba(0,0,0, 70%);
    border-radius: 2rem;
    padding: 0.7rem 0.9rem;
    svg {
        font-size: 1.8rem;
        color: white;
        transition: 0.6s ease-in-out;
        &:hover {
            transform: scale(1.3);
        }
    }
`;

