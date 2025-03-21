with raw_survey as (
    select * from {{ source('airbyte_data', 'survey') }}
),

survey_transformed as (
    select
        {{ adapter.quote('TIMESTAMP') }} as survey_time,
        {{ adapter.quote('EMAIL_ADDRESS') }} as email,
        {{ adapter.quote('WHAT_IS_YOUR_AGE_') }} as age,
        {{ adapter.quote('WHICH_BEST_DESCRIBES_YOUR_PRIMARY_MAJOR_OR_FIELD_OF_STUDY_IF_YOU_HAVE_MORE_THAN_ONE_MAJOR_PLEASE_SPECIFY_OTHER_MAJORS_AS_PART_OF_THE_NEXT_QUESTION_') }} as primary_major,
        {{ adapter.quote('IF_YOU_HAVE_SECONDARY_MAJORS_PLEASE_LIST_THEM_HERE_SEPARATED_BY_A_COMMA_') }} as secondary_major 
    from raw_survey
)

select * from survey_transformed
