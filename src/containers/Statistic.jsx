import React, { useState } from 'react'
import { Button, DatePicker, Space } from 'antd';
import '../App.scss'
import StatisticImage from '../assets/thumbnail.png'

// import Axios from 'axios';
import axios from "axios";



const { RangePicker } = DatePicker;


const Statistic = () => {
    const [statisticData,setStatisticData] = useState(null);
    const [imageSrc,setImageSrc] = useState();
    const [startDate,setStartDate] = useState();
    const [endDate,setEndDate] = useState();

    const fetchStatistic = () => {
        axios.defaults.baseURL = 'http://127.0.0.1:8000';

        var config = {
            method: 'post',
            // url: 'http://127.0.0.1:8000/visualization/1/',
            url: '/visualization/1/',

            
            data : {
                start_date: new Date(startDate).toLocaleDateString('sv'),
                end_date: new Date(endDate).toLocaleDateString('sv'),
            }
        };

		
		return axios(config).then( (response) => {
            const urlImage = response.data.url_image;
            const ImageStore1 = require(`../assets/${urlImage}`)
            console.log(response)
            setImageSrc(ImageStore1);
          })
          .catch(function (error) {
            console.log(error);
          });;

        
    };

    const handleChangeStatistic = () => {

    }

    const handleRangePicker = (event) => {
        console.log(event)
        setStartDate(event[0].$d);
        setEndDate(event[1].$d);
    }


    return (
        <div className='statistic-main'>
            <div className='nav-bar'>
                <div className='nav-item'>
                    Theo x
                </div>
                <div className='nav-item'>
                    Theo x
                </div>
                <div className='nav-item'>
                    Theo x
                </div>
                <div className='nav-item'>
                    Theo x
                </div>
            </div>
            <div className='statistic-content'>
                <div className='select-area'>
                    <RangePicker 
                        className='range-picker'
                        onChange={
                            (val) => handleRangePicker(val)
                        }
                    />
                    <Button
                        onClick={fetchStatistic}
                    >Xem thống kê</Button>
                </div>
                <div className='statistic-diagram'>
                    <img src={imageSrc}/>
                </div>
            </div>
        </div>
    )
}

export default Statistic