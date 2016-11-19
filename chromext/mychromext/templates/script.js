$("document").ready(function(){
	$('#form2').submit(function(){
		$('#CourseSelectPage').addClass('hidden');
		$('#CourseInfoPage').removeClass('hidden');
		return false;
	});
});


$(function(){
    var $select = $("#myList1");
    var option='';
    var list=['AF_AM_ST','AFST','AMER_ST','ANTHRO','APP_PHYS','ARABIC','ART','ART_HIST','ASIAN_AM','ASIAN_LC','ASIAN_ST','ASTRON','ATHL_PRA','BIOL_SCI','BMD_ENG','BUS_INST','CFS','CHEM','CHEM_ENG','CHINESE','CHSS','CIV_ENV','CLASSICS','CLIN_PSY','CME','CMN','COG_SCI','COMM_ST','COMP_LIT','CONDUCT','COUN','CRDV','CSD','DANCE','DSGN','EARTH','ECON','EECS','ENGLISH','ENTREP','ENVR_POL','ENVR_SCI','EPI_BIO','ES_APPM','FRENCH','GAMS','GBL_HLTH','GEN_CMN','GEN_ENG','GENET_CN','GEN_MUS','GEOG','GERMAN','GNDR_ST','GREEK','HDPS','HDSP','HEBREW','HIND_URD','HISTORY','HLTH_COM','HQS','HSIP','HSR','HUM','IBIS','IEMS','IGP','IMC','INF_TECH','INTG_SCI','INTL_ST','ISEN','ITALIAN','JAPANESE','JAZZ_ST','JOUR','JWSH_ST','KELLG_FE','KELLG_MA','KOREAN','LATIN','LATINO','LDRSHP','LEGAL_ST','LING','LOC','LRN_SCI','MATH','MAT_SCI','MBIOTECH','MDVL_ST','MECH_ENG','MEM','MENA','MHB','MMSS','MSC','MSCI','MS_ED','MS_FT','MS_HE','MSIA','MSLCE','MS_LOC','MSTP','MTS','MUS_COMP','MUSIC','MUSIC_ED','MUSICOL','MUS_TECH','MUS_THRY','NAV_SCI','NEUROBIO','NEUROSCI','NICO','NUIN','PBC','PERF_ST','PERSIAN','PHIL','PHYSICS','PIANO','POLI_SCI','PORT','PRDV','PROJ_MGT','PSED','PSYCH','PUB_HLTH','RELIGION','REPR_SCI','RTVF','SESP','SHC','SLAVIC','SOCIOL','SOC_POL','SPANISH','SPANPORT','STAT','STRINGS','SWAHILI','TEACH_ED','TGS','TH&DRAMA','THEATRE','TURKISH','URBAN_ST','VOICE','WIND_PER']
	for (var i=0; i<list.length; i++){

		option += '<option value="'+ list[i] + '">' + list[i] + '</option>';
	}
	$select.append(option);

});
