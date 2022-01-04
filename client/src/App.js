import React, { useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import ES from './components/analysis/ES';
import Facility from './components/analysis/Facility';
import Population from './components/analysis/Population';
import Revenue from './components/analysis/Revenue';
import Sector from './components/analysis/Sector';
import Summary from './components/analysis/Summary';
import Footer from './components/Footer';
import NavBar from './components/NavBar';
import Overview from './components/Overview';
import ScrollToTop from './components/ScrollToTop';

const CITY_IDS = [
  '11740', '11710', '11680', '11650', '11620', '11590', '11560', '11545',
  '11530', '11500', '11470', '11440', '11410', '11380', '11350', '11320',
  '11305', '11290', '11260', '11230', '11215', '11200', '11170', '11140',
  '11110',
];

export default function App() {
  let { cityId } = useParams();
  const navigate = useNavigate();
  cityId = CITY_IDS.includes(cityId) ? cityId : null;

  useEffect(() => {
    if (!cityId) {
      navigate("/", {replace: true});
    }
  }, [cityId, navigate])

  return (
    <div>
      <ScrollToTop/>
      <NavBar/>
      <Overview cityId={cityId}/>
      <Summary cityId={cityId}/>
      <Revenue cityId={cityId}/>
      <Population cityId={cityId}/>
      <Sector cityId={cityId}/>
      <Facility cityId={cityId}/>
      <ES cityId={cityId}/>
      <Footer/>
    </div>
  );
}