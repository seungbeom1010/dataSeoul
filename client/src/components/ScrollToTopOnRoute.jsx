import { useEffect } from "react";
import { useLocation } from "react-router-dom";

export default function ScrollToTopOnRoute() {
  const { pathname } = useLocation();

  // pathname 변경 시 랜더링 이후 window.scrollTo(0, 0)으로 이동

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [pathname]);
  
  return null;
}