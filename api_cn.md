# 共享类型

```python
from openai.types import (
    AllModels,
    ChatModel,
    ComparisonFilter,
    CompoundFilter,
    CustomToolInputFormat,
    ErrorObject,
    FunctionDefinition,
    FunctionParameters,
    Metadata,
    Reasoning,
    ReasoningEffort,
    ResponseFormatJSONObject,
    ResponseFormatJSONSchema,
    ResponseFormatText,
    ResponseFormatTextGrammar,
    ResponseFormatTextPython,
    ResponsesModel,
)
```

# 补全（Completions）

类型：

```python
from openai.types import Completion, CompletionChoice, CompletionUsage
```

方法：

- <code title="post /completions">client.completions.<a href="./src/openai/resources/completions.py">create</a>(\*\*<a href="src/openai/types/completion_create_params.py">params</a>) -> <a href="./src/openai/types/completion.py">Completion</a></code>

# 聊天（Chat）

类型：

```python
from openai.types import ChatModel
```

## 补全（Completions）

类型：

```python
from openai.types.chat import (
    ChatCompletion,
    ChatCompletionAllowedToolChoice,
    ChatCompletionAssistantMessageParam,
    ChatCompletionAudio,
    ChatCompletionAudioParam,
    ChatCompletionChunk,
    ChatCompletionContentPart,
    ChatCompletionContentPartImage,
    ChatCompletionContentPartInputAudio,
    ChatCompletionContentPartRefusal,
    ChatCompletionContentPartText,
    ChatCompletionCustomTool,
    ChatCompletionDeleted,
    ChatCompletionDeveloperMessageParam,
    ChatCompletionFunctionCallOption,
    ChatCompletionFunctionMessageParam,
    ChatCompletionFunctionTool,
    ChatCompletionMessage,
    ChatCompletionMessageCustomToolCall,
    ChatCompletionMessageFunctionToolCall,
    ChatCompletionMessageParam,
    ChatCompletionMessageToolCallUnion,
    ChatCompletionModality,
    ChatCompletionNamedToolChoice,
    ChatCompletionNamedToolChoiceCustom,
    ChatCompletionPredictionContent,
    ChatCompletionRole,
    ChatCompletionStoreMessage,
    ChatCompletionStreamOptions,
    ChatCompletionSystemMessageParam,
    ChatCompletionTokenLogprob,
    ChatCompletionToolUnion,
    ChatCompletionToolChoiceOption,
    ChatCompletionToolMessageParam,
    ChatCompletionUserMessageParam,
    ChatCompletionAllowedTools,
    ChatCompletionReasoningEffort,
)
```

方法：

- <code title="post /chat/completions">client.chat.completions.<a href="./src/openai/resources/chat/completions/completions.py">create</a>(\*\*<a href="src/openai/types/chat/completion_create_params.py">params</a>) -> <a href="./src/openai/types/chat/chat_completion.py">ChatCompletion</a></code>
- <code title="get /chat/completions/{completion_id}">client.chat.completions.<a href="./src/openai/resources/chat/completions/completions.py">retrieve</a>(completion_id) -> <a href="./src/openai/types/chat/chat_completion.py">ChatCompletion</a></code>
- <code title="post /chat/completions/{completion_id}">client.chat.completions.<a href="./src/openai/resources/chat/completions/completions.py">update</a>(completion_id, \*\*<a href="src/openai/types/chat/completion_update_params.py">params</a>) -> <a href="./src/openai/types/chat/chat_completion.py">ChatCompletion</a></code>
- <code title="get /chat/completions">client.chat.completions.<a href="./src/openai/resources/chat/completions/completions.py">list</a>(\*\*<a href="src/openai/types/chat/completion_list_params.py">params</a>) -> <a href="./src/openai/types/chat/chat_completion.py">SyncCursorPage[ChatCompletion]</a></code>
- <code title="delete /chat/completions/{completion_id}">client.chat.completions.<a href="./src/openai/resources/chat/completions/completions.py">delete</a>(completion_id) -> <a href="./src/openai/types/chat/chat_completion_deleted.py">ChatCompletionDeleted</a></code>

### 消息（Messages）

方法：

- <code title="get /chat/completions/{completion_id}/messages">client.chat.completions.messages.<a href="./src/openai/resources/chat/completions/messages.py">list</a>(completion_id, \*\*<a href="src/openai/types/chat/completions/message_list_params.py">params</a>) -> <a href="./src/openai/types/chat/chat_completion_store_message.py">SyncCursorPage[ChatCompletionStoreMessage]</a></code>

# 嵌入（Embeddings）

类型：

```python
from openai.types import CreateEmbeddingResponse, Embedding, EmbeddingModel
```

方法：

- <code title="post /embeddings">client.embeddings.<a href="./src/openai/resources/embeddings.py">create</a>(\*\*<a href="src/openai/types/embedding_create_params.py">params</a>) -> <a href="./src/openai/types/create_embedding_response.py">CreateEmbeddingResponse</a></code>

# 文件（Files）

类型：

```python
from openai.types import FileContent, FileDeleted, FileObject, FilePurpose
```

方法：

- <code title="post /files">client.files.<a href="./src/openai/resources/files.py">create</a>(\*\*<a href="src/openai/types/file_create_params.py">params</a>) -> <a href="./src/openai/types/file_object.py">FileObject</a></code>
- <code title="get /files/{file_id}">client.files.<a href="./src/openai/resources/files.py">retrieve</a>(file_id) -> <a href="./src/openai/types/file_object.py">FileObject</a></code>
- <code title="get /files">client.files.<a href="./src/openai/resources/files.py">list</a>(\*\*<a href="src/openai/types/file_list_params.py">params</a>) -> <a href="./src/openai/types/file_object.py">SyncCursorPage[FileObject]</a></code>
- <code title="delete /files/{file_id}">client.files.<a href="./src/openai/resources/files.py">delete</a>(file_id) -> <a href="./src/openai/types/file_deleted.py">FileDeleted</a></code>
- <code title="get /files/{file_id}/content">client.files.<a href="./src/openai/resources/files.py">content</a>(file_id) -> HttpxBinaryResponseContent</code>
- <code title="get /files/{file_id}/content">client.files.<a href="./src/openai/resources/files.py">retrieve_content</a>(file_id) -> <a href="./src/openai/types/file_content.py">str</a></code>
- <code>client.files.<a href="./src/openai/resources/files.py">wait_for_processing</a>(\*args) -> FileObject</code>

# 图像（Images）

类型：

```python
from openai.types import (
    Image,
    ImageEditCompletedEvent,
    ImageEditPartialImageEvent,
    ImageEditStreamEvent,
    ImageGenCompletedEvent,
    ImageGenPartialImageEvent,
    ImageGenStreamEvent,
    ImageModel,
    ImagesResponse,
)
```

方法：

- <code title="post /images/variations">client.images.<a href="./src/openai/resources/images.py">create_variation</a>(\*\*<a href="src/openai/types/image_create_variation_params.py">params</a>) -> <a href="./src/openai/types/images_response.py">ImagesResponse</a></code>
- <code title="post /images/edits">client.images.<a href="./src/openai/resources/images.py">edit</a>(\*\*<a href="src/openai/types/image_edit_params.py">params</a>) -> <a href="./src/openai/types/images_response.py">ImagesResponse</a></code>
- <code title="post /images/generations">client.images.<a href="./src/openai/resources/images.py">generate</a>(\*\*<a href="src/openai/types/image_generate_params.py">params</a>) -> <a href="./src/openai/types/images_response.py">ImagesResponse</a></code>

# 音频（Audio）

类型：

```python
from openai.types import AudioModel, AudioResponseFormat
```

## 转录（Transcriptions）

类型：

```python
from openai.types.audio import (
    Transcription,
    TranscriptionInclude,
    TranscriptionSegment,
    TranscriptionStreamEvent,
    TranscriptionTextDeltaEvent,
    TranscriptionTextDoneEvent,
    TranscriptionVerbose,
    TranscriptionWord,
    TranscriptionCreateResponse,
)
```

方法：

- <code title="post /audio/transcriptions">client.audio.transcriptions.<a href="./src/openai/resources/audio/transcriptions.py">create</a>(\*\*<a href="src/openai/types/audio/transcription_create_params.py">params</a>) -> <a href="./src/openai/types/audio/transcription_create_response.py">TranscriptionCreateResponse</a></code>

## 翻译（Translations）

类型：

```python
from openai.types.audio import Translation, TranslationVerbose, TranslationCreateResponse
```

方法：

- <code title="post /audio/translations">client.audio.translations.<a href="./src/openai/resources/audio/translations.py">create</a>(\*\*<a href="src/openai/types/audio/translation_create_params.py">params</a>) -> <a href="./src/openai/types/audio/translation_create_response.py">TranslationCreateResponse</a></code>

## 语音（Speech）

类型：

```python
from openai.types.audio import SpeechModel
```

方法：

- <code title="post /audio/speech">client.audio.speech.<a href="./src/openai/resources/audio/speech.py">create</a>(\*\*<a href="src/openai/types/audio/speech_create_params.py">params</a>) -> HttpxBinaryResponseContent</code>

# 内容审核（Moderations）

类型：

```python
from openai.types import (
    Moderation,
    ModerationImageURLInput,
    ModerationModel,
    ModerationMultiModalInput,
    ModerationTextInput,
    ModerationCreateResponse,
)
```

方法：

- <code title="post /moderations">client.moderations.<a href="./src/openai/resources/moderations.py">create</a>(\*\*<a href="src/openai/types/moderation_create_params.py">params</a>) -> <a href="./src/openai/types/moderation_create_response.py">ModerationCreateResponse</a></code>

# 模型（Models）

类型：

```python
from openai.types import Model, ModelDeleted
```

方法：

- <code title="get /models/{model}">client.models.<a href="./src/openai/resources/models.py">retrieve</a>(model) -> <a href="./src/openai/types/model.py">Model</a></code>
- <code title="get /models">client.models.<a href="./src/openai/resources/models.py">list</a>() -> <a href="./src/openai/types/model.py">SyncPage[Model]</a></code>
- <code title="delete /models/{model}">client.models.<a href="./src/openai/resources/models.py">delete</a>(model) -> <a href="./src/openai/types/model_deleted.py">ModelDeleted</a></code>

# 微调（FineTuning）

## 方法（Methods）

类型：

```python
from openai.types.fine_tuning import (
    DpoHyperparameters,
    DpoMethod,
    ReinforcementHyperparameters,
    ReinforcementMethod,
    SupervisedHyperparameters,
    SupervisedMethod,
)
```

## 任务（Jobs）

类型：

```python
from openai.types.fine_tuning import (
    FineTuningJob,
    FineTuningJobEvent,
    FineTuningJobWandbIntegration,
    FineTuningJobWandbIntegrationObject,
    FineTuningJobIntegration,
)
```

方法：

- <code title="post /fine_tuning/jobs">client.fine_tuning.jobs.<a href="./src/openai/resources/fine_tuning/jobs/jobs.py">create</a>(\*\*<a href="src/openai/types/fine_tuning/job_create_params.py">params</a>) -> <a href="./src/openai/types/fine_tuning/fine_tuning_job.py">FineTuningJob</a></code>
- <code title="get /fine_tuning/jobs/{fine_tuning_job_id}">client.fine_tuning.jobs.<a href="./src/openai/resources/fine_tuning/jobs/jobs.py">retrieve</a>(fine_tuning_job_id) -> <a href="./src/openai/types/fine_tuning/fine_tuning_job.py">FineTuningJob</a></code>
- <code title="get /fine_tuning/jobs">client.fine_tuning.jobs.<a href="./src/openai/resources/fine_tuning/jobs/jobs.py">list</a>(\*\*<a href="src/openai/types/fine_tuning/job_list_params.py">params</a>) -> <a href="./src/openai/types/fine_tuning/fine_tuning_job.py">SyncCursorPage[FineTuningJob]</a></code>
- <code title="post /fine_tuning/jobs/{fine_tuning_job_id}/cancel">client.fine_tuning.jobs.<a href="./src/openai/resources/fine_tuning/jobs/jobs.py">cancel</a>(fine_tuning_job_id) -> <a href="./src/openai/types/fine_tuning/fine_tuning_job.py">FineTuningJob</a></code>
- <code title="get /fine_tuning/jobs/{fine_tuning_job_id}/events">client.fine_tuning.jobs.<a href="./src/openai/resources/fine_tuning/jobs/jobs.py">list_events</a>(fine_tuning_job_id, \*\*<a href="src/openai/types/fine_tuning/job_list_events_params.py">params</a>) -> <a href="./src/openai/types/fine_tuning/fine_tuning_job_event.py">SyncCursorPage[FineTuningJobEvent]</a></code>
- <code title="post /fine_tuning/jobs/{fine_tuning_job_id}/pause">client.fine_tuning.jobs.<a href="./src/openai/resources/fine_tuning/jobs/jobs.py">pause</a>(fine_tuning_job_id) -> <a href="./src/openai/types/fine_tuning/fine_tuning_job.py">FineTuningJob</a></code>
- <code title="post /fine_tuning/jobs/{fine_tuning_job_id}/resume">client.fine_tuning.jobs.<a href="./src/openai/resources/fine_tuning/jobs/jobs.py">resume</a>(fine_tuning_job_id) -> <a href="./src/openai/types/fine_tuning/fine_tuning_job.py">FineTuningJob</a></code>

### 检查点（Checkpoints）

类型：

```python
from openai.types.fine_tuning.jobs import FineTuningJobCheckpoint
```

方法：

- <code title="get /fine_tuning/jobs/{fine_tuning_job_id}/checkpoints">client.fine_tuning.jobs.checkpoints.<a href="./src/openai/resources/fine_tuning/jobs/checkpoints.py">list</a>(fine_tuning_job_id, \*\*<a href="src/openai/types/fine_tuning/jobs/checkpoint_list_params.py">params</a>) -> <a href="./src/openai/types/fine_tuning/jobs/fine_tuning_job_checkpoint.py">SyncCursorPage[FineTuningJobCheckpoint]</a></code>

## 检查点（Checkpoints）

### 权限（Permissions）

类型：

```python
from openai.types.fine_tuning.checkpoints import (
    PermissionCreateResponse,
    PermissionRetrieveResponse,
    PermissionDeleteResponse,
)
```

方法：

- <code title="post /fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions">client.fine_tuning.checkpoints.permissions.<a href="./src/openai/resources/fine_tuning/checkpoints/permissions.py">create</a>(fine_tuned_model_checkpoint, \*\*<a href="src/openai/types/fine_tuning/checkpoints/permission_create_params.py">params</a>) -> <a href="./src/openai/types/fine_tuning/checkpoints/permission_create_response.py">SyncPage[PermissionCreateResponse]</a></code>
- <code title="get /fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions">client.fine_tuning.checkpoints.permissions.<a href="./src/openai/resources/fine_tuning/checkpoints/permissions.py">retrieve</a>(fine_tuned_model_checkpoint, \*\*<a href="src/openai/types/fine_tuning/checkpoints/permission_retrieve_params.py">params</a>) -> <a href="./src/openai/types/fine_tuning/checkpoints/permission_retrieve_response.py">PermissionRetrieveResponse</a></code>
- <code title="delete /fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions/{permission_id}">client.fine_tuning.checkpoints.permissions.<a href="./src/openai/resources/fine_tuning/checkpoints/permissions.py">delete</a>(permission_id, \*, fine_tuned_model_checkpoint) -> <a href="./src/openai/types/fine_tuning/checkpoints/permission_delete_response.py">PermissionDeleteResponse</a></code>

## Alpha 版本

### 评分器（Graders）

类型：

```python
from openai.types.fine_tuning.alpha import GraderRunResponse, GraderValidateResponse
```

方法：

- <code title="post /fine_tuning/alpha/graders/run">client.fine_tuning.alpha.graders.<a href="./src/openai/resources/fine_tuning/alpha/graders.py">run</a>(\*\*<a href="src/openai/types/fine_tuning/alpha/grader_run_params.py">params</a>) -> <a href="./src/openai/types/fine_tuning/alpha/grader_run_response.py">GraderRunResponse</a></code>
- <code title="post /fine_tuning/alpha/graders/validate">client.fine_tuning.alpha.graders.<a href="./src/openai/resources/fine_tuning/alpha/graders.py">validate</a>(\*\*<a href="src/openai/types/fine_tuning/alpha/grader_validate_params.py">params</a>) -> <a href="./src/openai/types/fine_tuning/alpha/grader_validate_response.py">GraderValidateResponse</a></code>

# 评分器（Graders）

## 评分器模型（GraderModels）

类型：

```python
from openai.types.graders import (
    LabelModelGrader,
    MultiGrader,
    PythonGrader,
    ScoreModelGrader,
    StringCheckGrader,
    TextSimilarityGrader,
)
```

# 向量存储（VectorStores）

类型：

```python
from openai.types import (
    AutoFileChunkingStrategyParam,
    FileChunkingStrategy,
    FileChunkingStrategyParam,
    OtherFileChunkingStrategyObject,
    StaticFileChunkingStrategy,
    StaticFileChunkingStrategyObject,
    StaticFileChunkingStrategyObjectParam,
    VectorStore,
    VectorStoreDeleted,
    VectorStoreSearchResponse,
)
```

方法：

- <code title="post /vector_stores">client.vector_stores.<a href="./src/openai/resources/vector_stores/vector_stores.py">create</a>(\*\*<a href="src/openai/types/vector_store_create_params.py">params</a>) -> <a href="./src/openai/types/vector_store.py">VectorStore</a></code>
- <code title="get /vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/openai/resources/vector_stores/vector_stores.py">retrieve</a>(vector_store_id) -> <a href="./src/openai/types/vector_store.py">VectorStore</a></code>
- <code title="post /vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/openai/resources/vector_stores/vector_stores.py">update</a>(vector_store_id, \*\*<a href="src/openai/types/vector_store_update_params.py">params</a>) -> <a href="./src/openai/types/vector_store.py">VectorStore</a></code>
- <code title="get /vector_stores">client.vector_stores.<a href="./src/openai/resources/vector_stores/vector_stores.py">list</a>(\*\*<a href="src/openai/types/vector_store_list_params.py">params</a>) -> <a href="./src/openai/types/vector_store.py">SyncCursorPage[VectorStore]</a></code>
- <code title="delete /vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/openai/resources/vector_stores/vector_stores.py">delete</a>(vector_store_id) -> <a href="./src/openai/types/vector_store_deleted.py">VectorStoreDeleted</a></code>
- <code title="post /vector_stores/{vector_store_id}/search">client.vector_stores.<a href="./src/openai/resources/vector_stores/vector_stores.py">search</a>(vector_store_id, \*\*<a href="src/openai/types/vector_store_search_params.py">params</a>) -> <a href="./src/openai/types/vector_store_search_response.py">SyncPage[VectorStoreSearchResponse]</a></code>

## 文件（Files）

类型：

```python
from openai.types.vector_stores import VectorStoreFile, VectorStoreFileDeleted, FileContentResponse
```

方法：

- <code title="post /vector_stores/{vector_store_id}/files">client.vector_stores.files.<a href="./src/openai/resources/vector_stores/files.py">create</a>(vector_store_id, \*\*<a href="src/openai/types/vector_stores/file_create_params.py">params</a>) -> <a href="./src/openai/types/vector_stores/vector_store_file.py">VectorStoreFile</a></code>
- <code title="get /vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/openai/resources/vector_stores/files.py">retrieve</a>(file_id, \*, vector_store_id) -> <a href="./src/openai/types/vector_stores/vector_store_file.py">VectorStoreFile</a></code>
- <code title="post /vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/openai/resources/vector_stores/files.py">update</a>(file_id, \*, vector_store_id, \*\*<a href="src/openai/types/vector_stores/file_update_params.py">params</a>) -> <a href="./src/openai/types/vector_stores/vector_store_file.py">VectorStoreFile</a></code>
- <code title="get /vector_stores/{vector_store_id}/files">client.vector_stores.files.<a href="./src/openai/resources/vector_stores/files.py">list</a>(vector_store_id, \*\*<a href="src/openai/types/vector_stores/file_list_params.py">params</a>) -> <a href="./src/openai/types/vector_stores/vector_store_file.py">SyncCursorPage[VectorStoreFile]</a></code>
- <code title="delete /vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/openai/resources/vector_stores/files.py">delete</a>(file_id, \*, vector_store_id) -> <a href="./src/openai/types/vector_stores/vector_store_file_deleted.py">VectorStoreFileDeleted</a></code>
- <code title="get /vector_stores/{vector_store_id}/files/{file_id}/content">client.vector_stores.files.<a href="./src/openai/resources/vector_stores/files.py">content</a>(file_id, \*, vector_store_id) -> <a href="./src/openai/types/vector_stores/file_content_response.py">SyncPage[FileContentResponse]</a></code>
- <code>client.vector_stores.files.<a href="./src/openai/resources/vector_stores/files.py">create_and_poll</a>(\*args) -> VectorStoreFile</code>
- <code>client.vector_stores.files.<a href="./src/openai/resources/vector_stores/files.py">poll</a>(\*args) -> VectorStoreFile</code>
- <code>client.vector_stores.files.<a href="./src/openai/resources/vector_stores/files.py">upload</a>(\*args) -> VectorStoreFile</code>
- <code>client.vector_stores.files.<a href="./src/openai/resources/vector_stores/files.py">upload_and_poll</a>(\*args) -> VectorStoreFile</code>

## 文件批处理（FileBatches）

类型：

```python
from openai.types.vector_stores import VectorStoreFileBatch
```

方法：

- <code title="post /vector_stores/{vector_store_id}/file_batches">client.vector_stores.file_batches.<a href="./src/openai/resources/vector_stores/file_batches.py">create</a>(vector_store_id, \*\*<a href="src/openai/types/vector_stores/file_batch_create_params.py">params</a>) -> <a href="./src/openai/types/vector_stores/vector_store_file_batch.py">VectorStoreFileBatch</a></code>