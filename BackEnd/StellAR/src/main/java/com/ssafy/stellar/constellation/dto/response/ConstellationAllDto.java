package com.ssafy.stellar.constellation.dto.response;

import lombok.Getter;
import lombok.Setter;

import java.util.Date;

@Getter
@Setter
public class ConstellationAllDto {

    private String constellationId;
    private String constellationSeason;
    private String constellationDesc;
    private String constellationSubName;
    private Date constellationStartObservation;
    private String constellationImg;
    private String constellationStory;
    private String constellationType;
    private Date constellationEndObservation;

}
