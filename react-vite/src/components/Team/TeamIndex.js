import {useEffect} from 'react';
import {useDispatch, useSelector} from 'react-redux';
// import { getAllLeagues } from '../../redux/league';
import { useParams } from 'react-router-dom';
import { fetchAllLeagues } from "../../redux/league"
import OwnedLeagues from './OwnedLeagues';
