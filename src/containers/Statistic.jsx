import React, { useState } from 'react'
import { Button, DatePicker, Select, Space } from 'antd';
import '../App.scss'

// import Axios from 'axios';
import axios from "axios";



const { RangePicker } = DatePicker;


const Statistic = () => {
    const [statType,setStatType] = useState( 1);

    const [imageSrc,setImageSrc] = useState();
    const [startDate,setStartDate] = useState();
    const [endDate,setEndDate] = useState();
    const [year,setYear] = useState();
    const [startYear, setStartYear] = useState();
    const [endYear, setEndYear] = useState();

    const fetchStatistic = () => {
        axios.defaults.baseURL = 'http://127.0.0.1:8000';


        if(statType===1){
            var config = {
                method: 'post',
                url: '/visualization/1/',
                data : {
                    start_date: new Date(startDate).toLocaleDateString('sv'),
                    end_date: new Date(endDate).toLocaleDateString('sv'),
                }
            };
            return axios(config).then( (response) => {
                handleInsertImage(response)
              })
              .catch(function (error) {
                console.log(error);
              });
        }
        else if(statType===4){
            var config = {
                method: 'post',
                url: '/visualization/4/',
                data : {
                    start_date: new Date(startDate).toLocaleDateString('sv'),
                    end_date: new Date(endDate).toLocaleDateString('sv'),
                }
            };
            return axios(config).then( (response) => {
                handleInsertImage(response)

              })
              .catch(function (error) {
                console.log(error);
              });
        }
        else if(statType===2){
            var config = {
                method: 'post',
                url: '/visualization/2/',
                data : {
                    year: new Date(year).getFullYear()
                }
            };
            return axios(config).then( (response) => {
                handleInsertImage(response)
              })
              .catch(function (error) {
                console.log(error);
              });
        }
        else if(statType===5){
            var config = {
                method: 'post',
                url: '/visualization/5/',
                data : {
                    year:  new Date(year).getFullYear()
                }
            };
            return axios(config).then( (response) => {
                handleInsertImage(response)

              })
              .catch(function (error) {
                console.log(error);
              });
        }
        else if(statType===3){
            var config = {
                method: 'post',
                url: '/visualization/3/',
                data : {
                    start_year: startYear,
                    end_year: endYear
                }
            };
            return axios(config).then( (response) => {
                handleInsertImage(response)

              })
              .catch(function (error) {
                console.log(error);
              });
        }
        else if(statType===6){
            var config = {
                method: 'post',
                url: '/visualization/6/',
                data : {
                    start_year: startYear,
                    end_year: endYear
                }
            };
            return axios(config).then( (response) => {
                handleInsertImage(response)

              })
              .catch(function (error) {
                console.log(error);
              });
        }
        
        

        
    };

    const handleInsertImage = (response) => {
        const urlImage = response.data.url_image;
        setTimeout(()=>{
            setImageSrc(require(`../image_visualization/${urlImage}`))
        }, 5000);

        
        console.log(response);
        
    }

    const handleChangeStatistic = () => {

    }

    const handleDateRangePicker = (event) => {
        console.log(event)
        setStartDate(event[0].$d);
        setEndDate(event[1].$d);
    }

    const handleYearPicker = (event) => {
        setYear(event)
    }

    const handleYearRangePicker = (event) => {
        console.log(event)
        setStartYear(event[0].$y
            )
        setEndYear(event[1].$y
            )
    }

    const handleChangeStatType = (type) => {
        setStatType(type)
        setImageSrc(undefined)
        // localStorage.setItem("statType",type)
        // window.location.reload

        // const element = document.getElementById("statistic-image");
        // element.remove();

        // var child = document.createElement('div');
        // child.innerHTML = "<img id='statistic-image' src={imageSrc}/>";

        // var parent = document.getElementById("statistic-image-father");

        // parent.appendChild(child);
    }


    return (
        <div className='statistic-main'>
            <div className='nav-bar'>
                <div className='nav-item' onClick={()=> handleChangeStatType(1)}>
                    Theo 1
                </div>
                <div className='nav-item' onClick={()=> handleChangeStatType(2)}>
                    Theo 2
                </div>
                <div className='nav-item' onClick={()=> handleChangeStatType(3)}>
                    Theo 3
                </div>
                <div className='nav-item' onClick={()=> handleChangeStatType(4)}>
                    Theo 4
                </div>
                <div className='nav-item' onClick={()=> handleChangeStatType(5)}>
                    Theo 5
                </div>
                <div className='nav-item' onClick={()=> handleChangeStatType(6)}>
                    Theo 6
                </div>
            </div>
            <div className='statistic-content'>
                <div className='select-area'>
                    {
                        (statType===1 || statType===4) && 
                        <RangePicker 
                            className='range-picker'
                            onChange={
                                (val) => handleDateRangePicker(val)
                            }
                        />
                    }
                    {
                        (statType===2 || statType===5) && 
                        <DatePicker picker="year"  onChange={
                            (val) => handleYearPicker(val)
                        }/>
                    }
                    {
                        (statType===3 || statType===6) && 
                        <RangePicker picker="year" onChange={
                            (val) => handleYearRangePicker(val)
                        }/>
                    }
                    <Button
                        onClick={fetchStatistic}
                    >Xem thống kê</Button>
                </div>
                <div id='statistic-image-father' className='statistic-diagram'>
                    <img id='statistic-image' src={imageSrc}/>
                </div>
            </div>
        </div>
    )
}

export default Statistic

